import { useEffect, useMemo, useState } from "react";

const ROOT = "/assets/production-art";
const SCENE_MANIFEST = `${ROOT}/open-office/open_office_scene_v013.json`;
const ASSET_VERSION = Date.now();
const DEFAULT_FRAME_SIZE = [300, 360];
const FALLBACK_FRAME_COUNTS = { idle: 4, walk: 8, typing: 6, seated: 4 };
const FRAME_MS = 110;
const WALK_SPEED = 145;
const SEAT_SPRITE_SIZE = [80, 80];
const SEAT_SPRITE_ORIGIN = [40, 70];

function actionName(mode) {
  return mode.split("_")[0];
}

function frameCount(metas, kind, mode) {
  const action = actionName(mode);
  const meta = metas?.[kind];
  return meta?.anchors?.[mode]?.frameCount || meta?.actions?.[action] || FALLBACK_FRAME_COUNTS[action] || 1;
}

function framePath(metas, kind, mode, frame) {
  const count = frameCount(metas, kind, mode);
  return `${ROOT}/characters/${kind}/sprites/${mode}/${String(frame % count).padStart(2, "0")}.png?v=${ASSET_VERSION}`;
}

function originForFrame(meta, mode, frame) {
  const [frameWidth, frameHeight] = meta?.frameSize || DEFAULT_FRAME_SIZE;
  const anchor = meta?.anchors?.[mode];
  const origins = anchor?.perFrameOrigins;
  if (origins?.length) return origins[frame % origins.length];
  return anchor?.origin || [frameWidth / 2, frameHeight - 30];
}

function navNodeMap(manifest) {
  return manifest.navNodes || manifest.navigation?.nodes || manifest.walkNodes || {};
}

function navEdgeList(manifest) {
  return manifest.navEdges || manifest.navigation?.edges || manifest.walkEdges || [];
}

function patrolRouteMap(manifest) {
  return manifest.navigation?.patrolRoutes || manifest.patrolRoutes || {};
}

function flattenedAnchors(manifest) {
  const groups = Object.values(manifest.anchors || {});
  const nested = groups.some((value) => value && typeof value === "object" && !Number.isFinite(value.x));
  if (!nested) return manifest.anchors || {};
  return groups.reduce((all, group) => ({ ...all, ...group }), {});
}

function pointSource(manifest, name) {
  return navNodeMap(manifest)[name] || flattenedAnchors(manifest)[name] || manifest.seatAnchors?.[name] || manifest.walkNodes?.[name];
}

function widthAtY(manifest, y) {
  const stops = [...Object.values(flattenedAnchors(manifest)), ...Object.values(navNodeMap(manifest))]
    .filter((point) => Number.isFinite(point.y) && Number.isFinite(point.widthPct))
    .sort((a, b) => a.y - b.y);
  if (!stops.length) return 5;
  if (y <= stops[0].y) return stops[0].widthPct;

  for (let index = 1; index < stops.length; index += 1) {
    const prev = stops[index - 1];
    const next = stops[index];
    if (y <= next.y) {
      const span = next.y - prev.y || 1;
      return prev.widthPct + ((next.widthPct - prev.widthPct) * (y - prev.y)) / span;
    }
  }

  return stops[stops.length - 1].widthPct;
}

function scenePoint(manifest, source, fallback = {}) {
  if (!source) return null;
  return {
    x: source.x,
    y: source.y,
    widthPct: source.widthPct ?? fallback.widthPct ?? widthAtY(manifest, source.y),
    z: source.z ?? fallback.z ?? Math.round(source.y / 18),
  };
}

function namedPoint(manifest, name) {
  return scenePoint(manifest, pointSource(manifest, name));
}

function targetPoint(manifest, target) {
  if (!target) return null;
  return scenePoint(
    manifest,
    target.point || pointSource(manifest, target.node) || pointSource(manifest, target.anchor),
  );
}

function distance(a, b) {
  return Math.hypot(b.x - a.x, b.y - a.y);
}

function samePoint(a, b) {
  return a && b && distance(a, b) < 1;
}

function lerpPoint(from, to, t) {
  return {
    x: from.x + (to.x - from.x) * t,
    y: from.y + (to.y - from.y) * t,
    widthPct: from.widthPct + (to.widthPct - from.widthPct) * t,
    z: Math.round(from.z + (to.z - from.z) * t),
  };
}

function walkMode(from, to) {
  const dx = to.x - from.x;
  const dy = to.y - from.y;
  const direction = dy >= 0 ? (dx >= 0 ? "SE" : "SW") : dx >= 0 ? "NE" : "NW";
  return `walk_${direction}`;
}

function idleMode(mode, fallback = "NE") {
  return `idle_${mode.split("_")[1] || fallback}`;
}

function hashString(value) {
  return String(value).split("").reduce((sum, char) => ((sum << 5) - sum + char.charCodeAt(0)) | 0, 0);
}

function seatPalette(actor) {
  const jackets = actor.gender === "female"
    ? ["#263e73", "#42315f", "#1f5a59", "#5a3446", "#27495f", "#4c3d24", "#394b72"]
    : ["#1d3768", "#253550", "#244646", "#3d3d4d", "#2c4968", "#3a344f", "#26413d"];
  const shirts = ["#e8edf1", "#d7e6e2", "#eadfcf", "#d8ddea", "#efe7d4"];
  const hair = actor.gender === "female"
    ? ["#261c1a", "#422820", "#15191d", "#5a3829"]
    : ["#14191e", "#2b211d", "#1e2427", "#38271d"];
  const skin = ["#d7a178", "#c98d68", "#e0b289", "#b87858", "#d7a98b"];
  const seed = Math.abs(hashString(actor.id));
  return {
    jacket: jackets[seed % jackets.length],
    shirt: shirts[(seed >> 2) % shirts.length],
    hair: hair[(seed >> 4) % hair.length],
    skin: skin[(seed >> 6) % skin.length],
    variant: seed % 5,
  };
}

function graphNodeIds(manifest) {
  return Object.keys(navNodeMap(manifest));
}

function graphEdges(manifest) {
  return navEdgeList(manifest);
}

function nearestNode(manifest, point) {
  return graphNodeIds(manifest).reduce((best, id) => {
    const node = namedPoint(manifest, id);
    if (!node) return best;
    const score = distance(point, node);
    return !best || score < best.score ? { id, score } : best;
  }, null)?.id;
}

function pathfind(manifest, fromId, toId) {
  if (!fromId || !toId) return [];
  if (fromId === toId) return [fromId];

  const neighbors = new Map(graphNodeIds(manifest).map((id) => [id, []]));
  graphEdges(manifest).forEach(([a, b]) => {
    if (!neighbors.has(a) || !neighbors.has(b)) return;
    neighbors.get(a).push(b);
    neighbors.get(b).push(a);
  });

  const queue = [fromId];
  const prev = new Map([[fromId, null]]);
  for (let head = 0; head < queue.length; head += 1) {
    const id = queue[head];
    for (const next of neighbors.get(id) || []) {
      if (prev.has(next)) continue;
      prev.set(next, id);
      if (next === toId) {
        const path = [toId];
        while (path[0] !== fromId) path.unshift(prev.get(path[0]));
        return path;
      }
      queue.push(next);
    }
  }

  return [];
}

function startMove(current, target, manifest, now) {
  const targetNode = target.node;
  if (!targetNode) return current;
  const currentNode = current.nodeId || nearestNode(manifest, current.point);
  const nodePath = pathfind(manifest, currentNode, targetNode);
  const route = nodePath.map((id) => ({ id, point: namedPoint(manifest, id) })).filter((item) => item.point);
  const targets = route.filter((item) => !samePoint(current.point, item.point));
  const next = targets[0];

  if (!next) {
    return {
      ...current,
      activeTargetId: target.id,
      arriveMode: target.idleMode || idleMode(current.mode),
      mode: target.idleMode || idleMode(current.mode),
      modeStarted: now,
      moving: false,
      nodeId: targetNode || current.nodeId,
      officeLabel: target.label,
      phase: "idle",
    };
  }

  return {
    ...current,
    activeTargetId: target.id,
    arriveMode: target.idleMode || idleMode(walkMode(current.point, next.point)),
    mode: walkMode(current.point, next.point),
    modeStarted: now,
    moving: true,
    nextNodeId: next.id,
    nodeId: currentNode,
    officeLabel: target.label,
    phase: "walking",
    route: targets.slice(1),
    segmentDuration: Math.max(160, (distance(current.point, next.point) / WALK_SPEED) * 1000),
    segmentFrom: current.point,
    segmentStart: now,
    segmentTo: next.point,
  };
}

function advanceLead(current, now) {
  if (!current || current.phase !== "walking") return current;

  const t = (now - current.segmentStart) / current.segmentDuration;
  if (t < 1) return { ...current, point: lerpPoint(current.segmentFrom, current.segmentTo, t) };

  if (current.route?.length) {
    const next = current.route[0];
    return {
      ...current,
      mode: walkMode(current.segmentTo, next.point),
      modeStarted: now,
      nextNodeId: next.id,
      nodeId: current.nextNodeId,
      point: current.segmentTo,
      route: current.route.slice(1),
      segmentDuration: Math.max(160, (distance(current.segmentTo, next.point) / WALK_SPEED) * 1000),
      segmentFrom: current.segmentTo,
      segmentStart: now,
      segmentTo: next.point,
    };
  }

  return {
    ...current,
    mode: current.arriveMode || idleMode(current.mode),
    modeStarted: now,
    moving: false,
    nodeId: current.nextNodeId || current.nodeId,
    phase: "idle",
    point: current.segmentTo,
  };
}

function patrolPoints(manifest, routeId) {
  return (patrolRouteMap(manifest)[routeId] || [])
    .map((id) => ({ id, point: namedPoint(manifest, id) }))
    .filter((item) => item.point);
}

function createPatroller(person, manifest, now) {
  const route = patrolPoints(manifest, person.patrolRoute);
  const startPoint = namedPoint(manifest, person.anchor) || route[0]?.point;
  if (!route.length || !startPoint) return null;

  const startIndex = Math.max(0, route.findIndex((item) => item.id === person.anchor));
  const nextIndex = (startIndex + 1) % route.length;
  const segmentTo = route[nextIndex]?.point || startPoint;

  return {
    id: person.id,
    frameOffset: person.frameOffset || 0,
    kind: person.kind,
    mode: walkMode(startPoint, segmentTo),
    modeStarted: now,
    point: startPoint,
    route,
    routeIndex: startIndex,
    segmentDuration: Math.max(220, (distance(startPoint, segmentTo) / (person.speed || WALK_SPEED * 0.68)) * 1000),
    segmentFrom: startPoint,
    segmentStart: now,
    segmentTo,
    speed: person.speed || WALK_SPEED * 0.68,
  };
}

function advancePatroller(current, now) {
  if (!current?.route?.length) return current;

  const t = (now - current.segmentStart) / current.segmentDuration;
  if (t < 1) return { ...current, point: lerpPoint(current.segmentFrom, current.segmentTo, t) };

  const routeIndex = (current.routeIndex + 1) % current.route.length;
  const nextIndex = (routeIndex + 1) % current.route.length;
  const segmentFrom = current.segmentTo;
  const segmentTo = current.route[nextIndex]?.point || current.route[0].point;

  return {
    ...current,
    mode: walkMode(segmentFrom, segmentTo),
    modeStarted: now,
    point: segmentFrom,
    routeIndex,
    segmentDuration: Math.max(220, (distance(segmentFrom, segmentTo) / current.speed) * 1000),
    segmentFrom,
    segmentStart: now,
    segmentTo,
  };
}

function occupiedOccluders(manifest, people, seatActors) {
  const ids = new Set(manifest.sceneOccluders || []);

  people.forEach((person) => {
    manifest.seats?.find((seat) => seat.id === person.anchor)?.occluders?.forEach((id) => ids.add(id));
  });
  seatActors.forEach((actor) => {
    if (actor.renderMode === "vector-2.5d") return;
    actor.occluders?.forEach((id) => ids.add(id));
  });

  return Array.from(ids);
}

function SceneOccluder({ id, manifest }) {
  const occluder = manifest.occluders?.[id];
  if (!occluder) return null;
  return (
    <img
      alt=""
      className="art25d-layer art25d-occluder"
      src={`${ROOT}/${occluder.src}?v=${ASSET_VERSION}`}
      style={{ zIndex: occluder.z }}
    />
  );
}

function ScenePerson({ frame, kind, metas, mode, point, size }) {
  if (!point) return null;

  const meta = metas?.[kind];
  const [frameWidth] = meta?.frameSize || DEFAULT_FRAME_SIZE;
  const action = actionName(mode);
  const frameIndex = frame % frameCount(metas, kind, mode);
  const origin = originForFrame(meta, mode, frameIndex);
  const scale = (size[0] * (point.widthPct / 100)) / frameWidth;
  const left = point.x - origin[0] * scale;
  const top = point.y - origin[1] * scale;
  const feetY = point.y + (330 - origin[1]) * scale;
  const z = point.z ?? Math.round(point.y / 18);

  return (
    <>
      <span
        className={`person-shadow mode-${action}`}
        style={{
          left: `${(point.x / size[0]) * 100}%`,
          top: `${(feetY / size[1]) * 100}%`,
          width: `${point.widthPct * 0.7}%`,
          zIndex: z - 1,
        }}
      />
      <img
        alt=""
        className={`art25d-person mode-${action}`}
        src={framePath(metas, kind, mode, frameIndex)}
        style={{
          left: `${(left / size[0]) * 100}%`,
          top: `${(top / size[1]) * 100}%`,
          width: `${point.widthPct}%`,
          zIndex: z,
        }}
      />
    </>
  );
}

function SceneSeatActor({ actor, frame, size }) {
  const [frameWidth, frameHeight] = SEAT_SPRITE_SIZE;
  const origin = actor.spriteOrigin || SEAT_SPRITE_ORIGIN;
  const widthPct = actor.spriteWidthPct || actor.widthPct || 3.2;
  const widthPx = size[0] * (widthPct / 100);
  const scale = widthPx / frameWidth;
  const heightPx = frameHeight * scale;
  const left = actor.anchor.x - origin[0] * scale;
  const top = actor.anchor.y - origin[1] * scale;
  const palette = seatPalette(actor);
  const z = actor.z || Math.round(actor.anchor.y / 18);
  const sway = ((Math.abs(hashString(actor.id)) % 7) - 3) * 0.6;

  return (
    <svg
      aria-hidden="true"
      className={`seat-actor-layer seat-actor-svg gender-${actor.gender} facing-${actor.facing || "monitor_back"} variant-${palette.variant}`}
      data-seat-actor={actor.id}
      viewBox="0 0 80 80"
      style={{
        "--jacket": palette.jacket,
        "--shirt": palette.shirt,
        "--hair": palette.hair,
        "--skin": palette.skin,
        "--seat-delay": `${-(frame % 12) * 0.09 - palette.variant * 0.16}s`,
        "--seat-sway": `${sway}px`,
        height: `${(heightPx / size[1]) * 100}%`,
        left: `${(left / size[0]) * 100}%`,
        top: `${(top / size[1]) * 100}%`,
        width: `${widthPct}%`,
        zIndex: z,
      }}
    >
      <ellipse className="seat-svg-shadow" cx="40" cy="70" rx="24" ry="7" />
      <path className="seat-jacket" d="M20 70 C22 52 28 40 40 39 C52 40 58 52 60 70 Z" />
      <path className="seat-shirt" d="M34 41 L40 53 L46 41 C43 40 37 40 34 41 Z" />
      <path className="seat-shoulder seat-shoulder-left" d="M23 52 C27 45 32 42 37 42" />
      <path className="seat-shoulder seat-shoulder-right" d="M57 52 C53 45 48 42 43 42" />
      <g className="seat-arm seat-arm-left">
        <path d="M28 51 C25 57 25 62 30 66" />
        <ellipse cx="30" cy="66" rx="3.6" ry="2.6" />
      </g>
      <g className="seat-arm seat-arm-right">
        <path d="M52 51 C56 57 56 62 51 66" />
        <ellipse cx="51" cy="66" rx="3.6" ry="2.6" />
      </g>
      <path className="seat-neck" d="M35 37 C36 41 44 41 45 37 L45 43 C42 45 38 45 35 43 Z" />
      <ellipse className="seat-head" cx="40" cy="31" rx="10.2" ry="11.6" />
      {actor.gender === "female" ? (
        <>
          <path className="seat-hair seat-hair-back" d="M29 33 C28 20 34 13 40 13 C48 13 53 21 51 34 C50 45 45 50 40 51 C34 50 30 44 29 33 Z" />
          <path className="seat-hair seat-hair-crown" d="M30 27 C32 17 38 14 45 17 C50 20 51 26 50 32 C45 28 38 26 30 27 Z" />
        </>
      ) : (
        <>
          <path className="seat-hair seat-hair-back" d="M30 29 C30 20 34 15 41 15 C48 15 52 20 51 29 C46 26 38 25 30 29 Z" />
          <path className="seat-hair seat-hair-crown" d="M31 24 C35 16 47 16 50 25 C44 22 37 22 31 24 Z" />
        </>
      )}
      <path className="seat-collar" d="M33 42 L40 49 L47 42" />
      <path className="seat-key-action" d="M29 68 C35 70 45 70 52 68" />
    </svg>
  );
}

function zoneStyle(zone, size) {
  return {
    "--ambient-delay": `${zone.delay || 0}s`,
    "--ambient-duration": `${zone.duration || 4.8}s`,
    height: `${(zone.h / size[1]) * 100}%`,
    left: `${(zone.x / size[0]) * 100}%`,
    top: `${(zone.y / size[1]) * 100}%`,
    transform: zone.transform || "none",
    width: `${(zone.w / size[0]) * 100}%`,
    zIndex: zone.z || 24,
  };
}

function WindowTreeAnimation({ frame, manifest }) {
  const animation = manifest.ambientFx?.windowTreeAnimation;
  const [ready, setReady] = useState(false);

  useEffect(() => {
    if (!animation?.enabled || !animation.framePattern || typeof Image === "undefined") {
      setReady(false);
      return;
    }

    let cancelled = false;
    let pending = animation.frameCount;
    setReady(false);

    for (let index = 0; index < animation.frameCount; index += 1) {
      const frameName = String(index).padStart(2, "0");
      const image = new Image();
      image.onload = image.onerror = () => {
        pending -= 1;
        if (!cancelled && pending === 0) setReady(true);
      };
      image.src = `${ROOT}/${animation.framePattern.replace("{frame}", frameName)}?v=${animation.version || ASSET_VERSION}`;
    }

    return () => {
      cancelled = true;
    };
  }, [animation?.enabled, animation?.frameCount, animation?.framePattern, animation?.version]);

  if (!animation?.enabled || !animation.framePattern) return null;
  if (!ready) return null;

  const frameName = String(frame % animation.frameCount).padStart(2, "0");
  return (
    <img
      alt=""
      className="window-tree-animation"
      src={`${ROOT}/${animation.framePattern.replace("{frame}", frameName)}?v=${animation.version || ASSET_VERSION}`}
      style={{ zIndex: animation.z || 16 }}
    />
  );
}

function AmbientFx({ manifest }) {
  const fx = manifest.ambientFx || {};
  const size = manifest.size;

  return (
    <>
      {(fx.lightSweeps || []).map((zone) => (
        <span
          aria-hidden="true"
          className="ambient-fx ambient-light-sweep"
          key={zone.id}
          style={zoneStyle(zone, size)}
        />
      ))}
      {(fx.screenGlows || []).map((zone) => (
        <span
          aria-hidden="true"
          className="ambient-fx ambient-screen-glow"
          key={zone.id}
          style={zoneStyle(zone, size)}
        />
      ))}
      {(fx.shadowDrifts || []).map((zone) => (
        <span
          aria-hidden="true"
          className="ambient-fx ambient-shadow-drift"
          key={zone.id}
          style={zoneStyle(zone, size)}
        />
      ))}
    </>
  );
}

function NavDebug({ lead, manifest }) {
  const nodes = navNodeMap(manifest);
  const edges = navEdgeList(manifest);
  const path = lead?.moving
    ? [lead.point, lead.segmentTo, ...(lead.route || []).map((item) => item.point)].filter(Boolean)
    : [];

  return (
    <svg className="nav-debug" viewBox={`0 0 ${manifest.size[0]} ${manifest.size[1]}`} aria-hidden="true">
      {edges.map(([from, to]) => {
        const a = nodes[from];
        const b = nodes[to];
        if (!a || !b) return null;
        return <line className="nav-edge" key={`${from}-${to}`} x1={a.x} y1={a.y} x2={b.x} y2={b.y} />;
      })}
      {path.map((point, index) => {
        const next = path[index + 1];
        if (!next) return null;
        return <line className="nav-path" key={`${point.x}-${point.y}-${next.x}-${next.y}`} x1={point.x} y1={point.y} x2={next.x} y2={next.y} />;
      })}
      {Object.entries(nodes).map(([id, point]) => (
        <circle className="nav-node" key={id} cx={point.x} cy={point.y} r="7" />
      ))}
    </svg>
  );
}

export default function Art25DScene() {
  const [clock, setClock] = useState(0);
  const [lead, setLead] = useState(null);
  const [manifest, setManifest] = useState(null);
  const [metas, setMetas] = useState({});
  const [patrollers, setPatrollers] = useState([]);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      const scene = await fetch(`${SCENE_MANIFEST}?v=${ASSET_VERSION}`).then((response) => response.json());
      const people = scene.people || [];
      const kinds = Array.from(new Set(people.map((person) => person.kind)));
      const entries = await Promise.all(
        kinds.map(async (kind) => [
          kind,
          await fetch(`${ROOT}/characters/${kind}/sprite_meta.json?v=${ASSET_VERSION}`).then((response) => response.json()),
        ]),
      );
      if (cancelled) return;

      const now = performance.now();
      const interactive = people.find((person) => person.interactive) || people[0];
      const initialTarget = scene.officeTargets?.find((target) => target.id === interactive.targetId) || scene.officeTargets?.[0];
      setManifest(scene);
      setMetas(Object.fromEntries(entries));
      setPatrollers(people.filter((person) => person.patrolRoute).map((person) => createPatroller(person, scene, now)).filter(Boolean));
      setLead({
        activeTargetId: initialTarget?.id,
        kind: interactive.kind,
        mode: interactive.mode,
        modeStarted: now,
        moving: false,
        nodeId: interactive.anchor,
        officeLabel: initialTarget?.label || "",
        phase: "idle",
        point: namedPoint(scene, interactive.anchor) || targetPoint(scene, initialTarget),
      });
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    let timer = 0;

    function tick(now) {
      setClock(now);
      setLead((current) => advanceLead(current, now));
      setPatrollers((current) => current.map((patroller) => advancePatroller(patroller, now)));
      timer = requestAnimationFrame(tick);
    }

    timer = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(timer);
  }, []);

  const staticPeople = useMemo(
    () => manifest?.people.filter((person) => !person.interactive && !person.patrolRoute) || [],
    [manifest],
  );
  const useBakedStaff = Boolean(manifest?.layers?.fixedStaffBase);
  const seatActors = useMemo(
    () => (useBakedStaff ? [] : manifest?.seatActors?.filter((actor) => actor.ready) || []),
    [manifest, useBakedStaff],
  );
  const officeTargets = manifest?.officeTargets || [];

  const moveToTarget = (target) => {
    if (!manifest || !lead) return;
    setLead((current) => startMove(current, target, manifest, performance.now()));
  };

  if (!manifest || !lead) {
    return (
      <div className="art25d-scene is-loading">
        <span>加载 2.5D 美术分层</span>
      </div>
    );
  }

  const frame = Math.floor(clock / FRAME_MS);
  const windowTreeAnimation = manifest.ambientFx?.windowTreeAnimation;
  const windowTreeFrame = windowTreeAnimation
    ? Math.floor((clock / 1000) * (windowTreeAnimation.fps || 12)) % windowTreeAnimation.frameCount
    : 0;
  const leadFrame = Math.max(0, Math.floor((clock - lead.modeStarted) / FRAME_MS));
  const occluders = !useBakedStaff && manifest.occluders ? occupiedOccluders(manifest, staticPeople, seatActors) : [];

  return (
    <div className="art25d-scene">
      <div className="art25d-stage">
        <img alt="" className="art25d-layer" src={`${ROOT}/${manifest.layers.fixedStaffBase || manifest.layers.base}?v=${ASSET_VERSION}`} />
        {manifest.layers.foregroundCutout ? <img alt="" className="art25d-layer layer-foreground-cutout" src={`${ROOT}/${manifest.layers.foregroundCutout}?v=${ASSET_VERSION}`} /> : null}
        <WindowTreeAnimation frame={windowTreeFrame} manifest={manifest} />
        {manifest.layers.windowForeground ? <img alt="" className="art25d-layer layer-window-foreground" src={`${ROOT}/${manifest.layers.windowForeground}?v=${ASSET_VERSION}`} /> : null}
        <AmbientFx manifest={manifest} />
        {!useBakedStaff ? <img alt="" className="art25d-layer layer-shadow" src={`${ROOT}/${manifest.layers.shadow}?v=${ASSET_VERSION}`} /> : null}
        {manifest.debug?.nav ? <NavDebug lead={lead} manifest={manifest} /> : null}
        {seatActors.map((actor) => (
          <SceneSeatActor actor={actor} frame={frame} key={actor.id} size={manifest.size} />
        ))}
        {staticPeople.map((person) => (
          <ScenePerson
            frame={frame + (person.frameOffset || 0)}
            key={person.id}
            kind={person.kind}
            metas={metas}
            mode={person.mode}
            point={namedPoint(manifest, person.anchor)}
            size={manifest.size}
          />
        ))}
        {patrollers.map((person) => (
          <ScenePerson
            frame={Math.max(0, Math.floor((clock - person.modeStarted) / FRAME_MS)) + person.frameOffset}
            key={person.id}
            kind={person.kind}
            metas={metas}
            mode={person.mode}
            point={person.point}
            size={manifest.size}
          />
        ))}
        <ScenePerson
          frame={leadFrame}
          kind={lead.kind}
          metas={metas}
          mode={lead.mode}
          point={lead.point}
          size={manifest.size}
        />
        {!useBakedStaff && (occluders.length
          ? occluders.map((id) => <SceneOccluder id={id} key={id} manifest={manifest} />)
          : null)}
        {manifest.layers.foreground ? <img alt="" className="art25d-layer layer-foreground" src={`${ROOT}/${manifest.layers.foreground}?v=${ASSET_VERSION}`} /> : null}
        {!useBakedStaff && manifest.layers.glass ? <img alt="" className="art25d-layer layer-glass" src={`${ROOT}/${manifest.layers.glass}?v=${ASSET_VERSION}`} /> : null}
      </div>

      <div className="office-targets" aria-label="办公室移动">
        {officeTargets.map((target) => (
          <button
            className={lead.activeTargetId === target.id ? "is-active" : ""}
            key={target.id}
            onClick={() => moveToTarget(target)}
            type="button"
          >
            <span>{target.label}</span>
          </button>
        ))}
      </div>
      <span className="three-status">
        {lead.moving ? `移动到 ${lead.officeLabel}` : manifest.action?.status || "手动人员调度"}
      </span>
    </div>
  );
}
