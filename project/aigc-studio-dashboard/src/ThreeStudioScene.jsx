import { useEffect, useRef, useState } from "react";
import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

const partNames = [
  "body",
  "head",
  "hair",
  "leftEye",
  "rightEye",
  "leftArm",
  "rightArm",
  "leftHand",
  "rightHand",
  "skirt",
  "leftThigh",
  "rightThigh",
  "leftShin",
  "rightShin",
  "leftShoe",
  "rightShoe",
];

const fallbackAnchors = {
  seat_back_a: [-3.2, 0, -2.67],
  seat_back_b: [-1.2, 0, -2.67],
  seat_back_c: [0.8, 0, -2.67],
  seat_front_b: [3.15, 0, 0.9],
  seat_meet_a: [-3, 0, 1.04],
  seat_meet_b: [-2, 0, 2.04],
  seat_main: [0.92, 0, 0.86],
  walk_main_a: [-3.7, 0, 1.9],
  walk_main_b: [-1.4, 0, 1.55],
  walk_main_c: [0.5, 0, 1],
  walker_a: [3.9, 0, 2.45],
  walker_b: [2.3, 0, 2.3],
  walker_c: [1.1, 0, 2],
};

function loadGltf(loader, path) {
  return new Promise((resolve, reject) => loader.load(path, resolve, undefined, reject));
}

function anchor(root, name, rotation = 0) {
  const point = root.getObjectByName(name);
  const position = new THREE.Vector3(...fallbackAnchors[name]);
  if (point) point.getWorldPosition(position);
  return { position, rotation: point?.rotation.y ?? rotation };
}

function colorMesh(object, color) {
  if (!object?.isMesh || !color) return;
  object.material = object.material.clone();
  object.material.color?.set(color);
}

function makeCharacter(base, look = {}) {
  const character = base.clone(true);
  character.traverse((object) => {
    if (!object.isMesh) return;
    object.castShadow = true;
    object.receiveShadow = true;
    object.material = object.material.clone();
  });

  const parts = Object.fromEntries(partNames.map((name) => [name, character.getObjectByName(name)]));
  colorMesh(parts.body, look.shirt);
  colorMesh(parts.leftArm, look.shirt);
  colorMesh(parts.rightArm, look.shirt);
  colorMesh(parts.skirt, look.pants);
  colorMesh(parts.leftThigh, look.pants);
  colorMesh(parts.rightThigh, look.pants);
  colorMesh(parts.leftShin, look.pants);
  colorMesh(parts.rightShin, look.pants);
  colorMesh(parts.hair, look.hair);
  if (parts.skirt) parts.skirt.visible = Boolean(look.skirt);
  character.userData.parts = parts;
  return character;
}

function resetRotation(part) {
  if (part) part.rotation.set(0, 0, 0);
}

function setPart(part, position, rotation = [0, 0, 0]) {
  if (!part) return;
  part.position.set(...position);
  part.rotation.set(...rotation);
}

// ponytail: segmented GLB animation is enough for this page; swap to Blender-baked clips when a rigged character arrives.
function setPose(character, mode, phase = 0) {
  const p = character.userData.parts;
  const swing = Math.sin(phase) * 0.28;
  Object.values(p).forEach(resetRotation);

  if (mode === "sitting" || mode === "typing") {
    setPart(p.body, [0, 0.82, -0.02]);
    setPart(p.head, [0, 1.23, -0.02]);
    setPart(p.hair, [0, 1.32, -0.04]);
    setPart(p.leftEye, [-0.07, 1.25, 0.16]);
    setPart(p.rightEye, [0.07, 1.25, 0.16]);
    setPart(p.leftArm, [-0.27, 0.78, 0.16], [1.05 + Math.sin(phase) * 0.05, 0, -0.12]);
    setPart(p.rightArm, [0.27, 0.78, 0.16], [1.05 - Math.sin(phase) * 0.05, 0, 0.12]);
    setPart(p.leftHand, [-0.24, 0.6, 0.34], [0.4, 0, -0.08]);
    setPart(p.rightHand, [0.24, 0.6, 0.34], [0.4, 0, 0.08]);
    setPart(p.skirt, [0, 0.62, 0.12], [0.25, 0, 0]);
    setPart(p.leftThigh, [-0.11, 0.48, 0.22], [Math.PI / 2, 0, 0]);
    setPart(p.rightThigh, [0.11, 0.48, 0.22], [Math.PI / 2, 0, 0]);
    setPart(p.leftShin, [-0.11, 0.23, 0.47]);
    setPart(p.rightShin, [0.11, 0.23, 0.47]);
    setPart(p.leftShoe, [-0.11, 0.04, 0.52]);
    setPart(p.rightShoe, [0.11, 0.04, 0.52]);
    return;
  }

  setPart(p.body, [0, 1.02, 0]);
  setPart(p.head, [0, 1.43, 0]);
  setPart(p.hair, [0, 1.52, -0.02]);
  setPart(p.leftEye, [-0.07, 1.46, 0.18]);
  setPart(p.rightEye, [0.07, 1.46, 0.18]);
  setPart(p.leftArm, [-0.3, 1.0, 0], [mode === "walking" ? swing : 0.08, 0, 0.1]);
  setPart(p.rightArm, [0.3, 1.0, 0], [mode === "walking" ? -swing : -0.08, 0, -0.1]);
  setPart(p.leftHand, [-0.3, 0.72, 0.02], [mode === "walking" ? swing : 0, 0, 0]);
  setPart(p.rightHand, [0.3, 0.72, 0.02], [mode === "walking" ? -swing : 0, 0, 0]);
  setPart(p.skirt, [0, 0.68, 0]);
  setPart(p.leftThigh, [-0.11, 0.55, 0], [mode === "walking" ? -swing : 0, 0, 0]);
  setPart(p.rightThigh, [0.11, 0.55, 0], [mode === "walking" ? swing : 0, 0, 0]);
  setPart(p.leftShin, [-0.11, 0.22, 0], [mode === "walking" ? swing * 0.8 : 0, 0, 0]);
  setPart(p.rightShin, [0.11, 0.22, 0], [mode === "walking" ? -swing * 0.8 : 0, 0, 0]);
  setPart(p.leftShoe, [-0.11, 0.04, 0.07]);
  setPart(p.rightShoe, [0.11, 0.04, 0.07]);
}

function placeSeated(scene, base, spec) {
  const character = makeCharacter(base, spec.look);
  character.position.copy(spec.position).setY(0.18);
  character.rotation.y = spec.rotation;
  setPose(character, "typing", spec.phase);
  scene.add(character);
  return character;
}

function moveAlong(character, state, stateKey, targetKey, path, speed, delta) {
  const target = state[targetKey];
  const direction = target.clone().sub(character.position);
  direction.y = 0;
  const distance = direction.length();
  if (distance > 0.025) {
    direction.normalize();
    character.position.addScaledVector(direction, Math.min(distance, speed * delta));
    character.rotation.y = Math.atan2(direction.x, direction.z);
    return true;
  }
  state[stateKey] = (state[stateKey] + 1) % path.length;
  state[targetKey] = path[state[stateKey]].clone();
  return false;
}

export default function ThreeStudioScene() {
  const hostRef = useRef(null);
  const sceneRef = useRef(null);
  const [mode, setMode] = useState("加载3D资产");

  useEffect(() => {
    const host = hostRef.current;
    if (!host) return undefined;

    let disposed = false;
    let frame = 0;
    const scene = new THREE.Scene();
    scene.background = new THREE.Color("#e7f1ed");

    const camera = new THREE.OrthographicCamera(-6.5, 6.5, 4.3, -4.3, 0.1, 100);
    camera.position.set(6.9, 6.0, 8.1);
    camera.lookAt(0, 0.65, 0);

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(host.clientWidth, host.clientHeight);
    host.appendChild(renderer.domElement);

    scene.add(new THREE.HemisphereLight("#ffffff", "#9fb5ad", 1.25));
    const sun = new THREE.DirectionalLight("#fff0cf", 2.8);
    sun.position.set(-4.5, 8.2, 5.8);
    sun.castShadow = true;
    sun.shadow.mapSize.set(2048, 2048);
    sun.shadow.camera.left = -8;
    sun.shadow.camera.right = 8;
    sun.shadow.camera.top = 8;
    sun.shadow.camera.bottom = -8;
    scene.add(sun);

    const resize = new ResizeObserver(([entry]) => {
      const { width, height } = entry.contentRect;
      renderer.setSize(width, height);
      const aspect = width / height;
      camera.left = -4.65 * aspect;
      camera.right = 4.65 * aspect;
      camera.top = 4.65;
      camera.bottom = -4.65;
      camera.updateProjectionMatrix();
    });
    resize.observe(host);

    const loader = new GLTFLoader();
    const clock = new THREE.Clock();
    const raycaster = new THREE.Raycaster();
    const pointer = new THREE.Vector2();

    async function start() {
      const [officeAsset, characterAsset] = await Promise.all([
        loadGltf(loader, "/assets/3d/office.glb"),
        loadGltf(loader, "/assets/3d/character.glb"),
      ]);
      if (disposed) return;

      const office = officeAsset.scene;
      office.traverse((object) => {
        if (!object.isMesh) return;
        object.castShadow = true;
        object.receiveShadow = true;
      });
      scene.add(office);

      const baseCharacter = characterAsset.scene;
      const mainSeat = anchor(office, "seat_main");
      mainSeat.position.y = 0.18;
      const mainRoute = ["walk_main_a", "walk_main_b", "walk_main_c"].map((name) => anchor(office, name).position);
      const walkPath = ["walker_a", "walker_b", "walker_c"].map((name) => anchor(office, name).position);

      const seatTarget = new THREE.Mesh(
        new THREE.BoxGeometry(1.2, 1.2, 1.2),
        new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false }),
      );
      seatTarget.position.copy(mainSeat.position).setY(0.7);
      scene.add(seatTarget);

      const seatSpecs = [
        ["seat_back_a", 0, { shirt: "#21415d", pants: "#273746" }],
        ["seat_back_b", 1, { shirt: "#e8dfc9", pants: "#2f3b48", skirt: true, hair: "#211816" }],
        ["seat_back_c", 2, { shirt: "#324c65", pants: "#3a4a58" }],
        ["seat_front_b", 3, { shirt: "#456f87", pants: "#2d3b42", skirt: true, hair: "#2d1c18" }],
        ["seat_meet_a", 4, { shirt: "#e5e0cb", pants: "#4b5b4a", skirt: true, hair: "#332016" }],
        ["seat_meet_b", 5, { shirt: "#283d58", pants: "#242f3c" }],
      ].map(([name, phase, look]) => ({ ...anchor(office, name), phase, look }));
      const animatedSeated = seatSpecs.map((spec) => placeSeated(scene, baseCharacter, spec));

      const mainCharacter = makeCharacter(baseCharacter, { shirt: "#203a56", pants: "#263746", hair: "#111518" });
      mainCharacter.position.copy(mainRoute[0]);
      mainCharacter.rotation.y = Math.atan2(mainRoute[1].x - mainRoute[0].x, mainRoute[1].z - mainRoute[0].z);
      scene.add(mainCharacter);

      const walker = makeCharacter(baseCharacter, { shirt: "#4f7d91", pants: "#263746", skirt: true, hair: "#2e2019" });
      walker.position.copy(walkPath[0]);
      scene.add(walker);

      const state = {
        mode: "idle",
        routeIndex: 0,
        target: mainRoute[1].clone(),
        walkIndex: 1,
        walkTarget: walkPath[1].clone(),
      };

      function goSit() {
        state.mode = "walking";
        state.routeIndex = 1;
        state.target = mainRoute[1].clone();
        setMode("走向主工位");
      }

      function standUp() {
        state.mode = "leaving";
        state.routeIndex = mainRoute.length - 2;
        state.target = mainRoute[mainRoute.length - 2].clone();
        setMode("起身返回");
      }

      function onPointerDown(event) {
        const rect = renderer.domElement.getBoundingClientRect();
        pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
        raycaster.setFromCamera(pointer, camera);
        if (!raycaster.intersectObject(seatTarget).length) return;
        if (state.mode === "sitting") standUp();
        else if (state.mode === "idle") goSit();
      }
      renderer.domElement.addEventListener("pointerdown", onPointerDown);

      function tick() {
        const delta = Math.min(clock.getDelta(), 0.04);
        const elapsed = clock.elapsedTime;

        animatedSeated.forEach((character, index) => setPose(character, "typing", elapsed * 2 + index));
        const walking = moveAlong(walker, state, "walkIndex", "walkTarget", walkPath, 0.8, delta);
        setPose(walker, walking ? "walking" : "idle", elapsed * 8);

        if (state.mode === "walking" || state.mode === "leaving") {
          const direction = state.target.clone().sub(mainCharacter.position);
          direction.y = 0;
          const distance = direction.length();
          if (distance > 0.025) {
            direction.normalize();
            mainCharacter.position.addScaledVector(direction, Math.min(distance, delta * 1.35));
            mainCharacter.rotation.y = Math.atan2(direction.x, direction.z);
            setPose(mainCharacter, "walking", elapsed * 9);
          } else if (state.mode === "walking" && state.routeIndex < mainRoute.length - 1) {
            state.routeIndex += 1;
            state.target = mainRoute[state.routeIndex].clone();
          } else if (state.mode === "walking") {
            state.mode = "sitting";
            mainCharacter.position.copy(mainSeat.position);
            mainCharacter.rotation.y = mainSeat.rotation;
            setPose(mainCharacter, "typing", elapsed * 3);
            setMode("坐下办公");
          } else if (state.routeIndex > 0) {
            state.routeIndex -= 1;
            state.target = mainRoute[state.routeIndex].clone();
          } else {
            state.mode = "idle";
            setPose(mainCharacter, "idle", elapsed * 4);
            setMode("明亮办公室 GLB");
          }
        } else {
          setPose(mainCharacter, state.mode === "sitting" ? "typing" : "idle", elapsed * 4);
        }

        renderer.render(scene, camera);
        frame = requestAnimationFrame(tick);
      }

      sceneRef.current = { state, goSit, standUp };
      setMode("明亮办公室 GLB");
      tick();

      return () => renderer.domElement.removeEventListener("pointerdown", onPointerDown);
    }

    let removePointer = () => {};
    start()
      .then((cleanup) => {
        if (cleanup) removePointer = cleanup;
      })
      .catch((error) => {
        console.error(error);
        setMode("3D资产加载失败");
      });

    return () => {
      disposed = true;
      cancelAnimationFrame(frame);
      removePointer();
      resize.disconnect();
      renderer.dispose();
      if (host.contains(renderer.domElement)) host.removeChild(renderer.domElement);
    };
  }, []);

  const toggle = () => {
    const api = sceneRef.current;
    if (!api) return;
    if (api.state.mode === "sitting") api.standUp();
    else if (api.state.mode === "idle") api.goSit();
  };

  return (
    <div className="three-scene">
      <div className="three-canvas" ref={hostRef} />
      <button className="three-action" onClick={toggle} type="button">{mode === "坐下办公" ? "起身" : "入座"}</button>
      <span className="three-status">{mode}</span>
    </div>
  );
}
