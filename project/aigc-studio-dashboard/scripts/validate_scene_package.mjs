import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const scenePath = path.join(root, "public/assets/production-art/scene/scene.json");
const sceneRoot = path.join(root, "public/assets/production-art");
const release = process.argv.includes("--release");

const scene = JSON.parse(fs.readFileSync(scenePath, "utf8"));
const errors = [];

function fail(message) {
  errors.push(message);
}

function exists(assetPath, label) {
  const file = path.join(sceneRoot, assetPath);
  if (!fs.existsSync(file)) fail(`${label} missing: ${assetPath}`);
}

function point(value, label) {
  if (!value || !Number.isFinite(value.x) || !Number.isFinite(value.y)) fail(`${label} needs numeric x/y`);
}

Object.entries(scene.layers || {}).forEach(([key, asset]) => {
  if (["walkableMask", "depthMap", "topViewControl"].includes(key)) return;
  exists(asset, `layer ${key}`);
});

Object.entries(scene.occluders || {}).forEach(([id, item]) => {
  exists(item.src, `occluder ${id}`);
  if (!Number.isFinite(item.z)) fail(`occluder ${id} needs z`);
});

const navNodes = scene.navNodes || {};
const navIds = new Set(Object.keys(navNodes));
if (!navIds.size) fail("navNodes required");
Object.entries(navNodes).forEach(([id, item]) => point(item, `navNodes.${id}`));
(scene.navEdges || []).forEach(([from, to], index) => {
  if (!navIds.has(from) || !navIds.has(to)) fail(`navEdges[${index}] references missing node`);
});

(scene.officeTargets || []).forEach((target) => {
  if (!navIds.has(target.node)) fail(`office target ${target.id} needs valid node`);
});

(scene.collisionZones || []).forEach((zone) => {
  if (!zone.id || !zone.kind) fail("collision zone needs id/kind");
  if (!Array.isArray(zone.polygon) || zone.polygon.length < 3) fail(`collision zone ${zone.id} needs polygon`);
  zone.polygon?.forEach((item, index) => point(item, `collisionZones.${zone.id}[${index}]`));
});

(scene.triggers || []).forEach((trigger) => {
  if (!trigger.id || !trigger.type) fail("trigger needs id/type");
  if (trigger.node && !navIds.has(trigger.node)) fail(`trigger ${trigger.id} references missing node`);
});

(scene.gameMarkers || []).forEach((marker) => {
  if (!marker.id || !marker.kind) fail("game marker needs id/kind");
  point(marker.point, `gameMarkers.${marker.id}.point`);
});

const seatActors = scene.seatActors || [];
if (!seatActors.length) fail("seatActors required for release-grade staffed scene");

const genders = { female: 0, male: 0 };
const actorIds = new Set();
seatActors.forEach((actor) => {
  if (!actor.id || actorIds.has(actor.id)) fail(`seat actor id invalid/duplicate: ${actor.id}`);
  actorIds.add(actor.id);
  if (!["female", "male"].includes(actor.gender)) fail(`seat actor ${actor.id} needs gender female/male`);
  else genders[actor.gender] += 1;
  point(actor.anchor, `seatActors.${actor.id}.anchor`);
  if (!actor.facing) fail(`seat actor ${actor.id} needs facing`);
  (actor.occluders || []).forEach((id) => {
    if (!scene.occluders?.[id]) fail(`seat actor ${actor.id} references missing occluder ${id}`);
  });
  if (release) {
    exists(actor.body, `seat actor ${actor.id} body`);
    if (!Array.isArray(actor.hands) || actor.hands.length < 2) fail(`seat actor ${actor.id} needs animated hands frames`);
    actor.hands?.forEach((asset, index) => exists(asset, `seat actor ${actor.id} hands[${index}]`));
  }
});

if (seatActors.length && genders.female !== genders.male) {
  fail(`seatActors gender split must be 50/50, got female=${genders.female} male=${genders.male}`);
}

if (errors.length) {
  console.error(errors.map((item) => `- ${item}`).join("\n"));
  process.exit(1);
}

console.log(`scene package ${release ? "release" : "contract"} ok: ${navIds.size} nav nodes, ${scene.navEdges?.length || 0} edges, ${seatActors.length} seat actors`);
