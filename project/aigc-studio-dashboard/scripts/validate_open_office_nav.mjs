import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const scenePath = path.join(root, "public/assets/production-art/open-office/open_office_scene_v002.json");
const scene = JSON.parse(fs.readFileSync(scenePath, "utf8"));
const nodes = scene.navigation?.nodes || {};
const errors = [];

function fail(message) {
  errors.push(message);
}

function pointOf(id) {
  const point = nodes[id];
  if (!point) fail(`missing nav node: ${id}`);
  return point && [point.x, point.y];
}

function pointInPolygon(point, polygon) {
  let inside = false;
  for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i, i += 1) {
    const a = polygon[i];
    const b = polygon[j];
    if ((a[1] > point[1]) !== (b[1] > point[1]) && point[0] < ((b[0] - a[0]) * (point[1] - a[1])) / (b[1] - a[1]) + a[0]) inside = !inside;
  }
  return inside;
}

function orientation(a, b, c) {
  return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
}

function onSegment(a, b, c) {
  return Math.min(a[0], b[0]) <= c[0] && c[0] <= Math.max(a[0], b[0])
    && Math.min(a[1], b[1]) <= c[1] && c[1] <= Math.max(a[1], b[1]);
}

function segmentsIntersect(a, b, c, d) {
  const o1 = orientation(a, b, c);
  const o2 = orientation(a, b, d);
  const o3 = orientation(c, d, a);
  const o4 = orientation(c, d, b);
  if (o1 === 0 && onSegment(a, b, c)) return true;
  if (o2 === 0 && onSegment(a, b, d)) return true;
  if (o3 === 0 && onSegment(c, d, a)) return true;
  if (o4 === 0 && onSegment(c, d, b)) return true;
  return (o1 > 0) !== (o2 > 0) && (o3 > 0) !== (o4 > 0);
}

// ponytail: fixed hand-authored corridor graph; upgrade to navmesh only if click-to-walk becomes real.
function segmentHitsZone(from, to, polygon) {
  if (pointInPolygon(from, polygon) || pointInPolygon(to, polygon)) return true;
  return polygon.some((point, index) => segmentsIntersect(from, to, point, polygon[(index + 1) % polygon.length]));
}

function checkSegment(label, fromId, toId) {
  const from = pointOf(fromId);
  const to = pointOf(toId);
  if (!from || !to) return;

  Object.entries(scene.collisionZones || {}).forEach(([zoneId, polygon]) => {
    if (segmentHitsZone(from, to, polygon)) fail(`${label} ${fromId} -> ${toId} crosses ${zoneId}`);
  });
}

Object.entries(nodes).forEach(([id, point]) => {
  Object.entries(scene.collisionZones || {}).forEach(([zoneId, polygon]) => {
    if (pointInPolygon([point.x, point.y], polygon)) fail(`node ${id} is inside ${zoneId}`);
  });
});

(scene.navigation?.edges || []).forEach(([from, to]) => checkSegment("edge", from, to));

Object.entries(scene.navigation?.patrolRoutes || {}).forEach(([routeId, route]) => {
  route.forEach((id, index) => {
    if (index) checkSegment(`patrol ${routeId}`, route[index - 1], id);
  });
});

(scene.officeTargets || []).forEach((target) => {
  if (!nodes[target.node]) fail(`office target ${target.id} needs valid node`);
});

if (errors.length) {
  console.error(errors.map((item) => `- ${item}`).join("\n"));
  process.exit(1);
}

console.log(`open office nav ok: ${Object.keys(nodes).length} nodes, ${scene.navigation?.edges?.length || 0} edges`);
