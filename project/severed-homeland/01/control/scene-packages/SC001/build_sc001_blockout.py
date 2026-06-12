"""
Build and export the SC001 blockout scene.

Run from the repository root or this directory with Blender:
  blender --background --python project/severed-homeland/01/control/scene-packages/SC001/build_sc001_blockout.py

The script intentionally has no PyYAML dependency. It mirrors
layout.yaml so the generated Blender scene is reproducible even in a
clean Blender Python environment.
"""

from __future__ import annotations

import json
import math
import os
import shutil
from pathlib import Path

import bpy
from mathutils import Vector


SCENE_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCENE_DIR.parents[5]
OUTPUTS = {
    "blend": SCENE_DIR / "blockout.blend",
    "top_view": SCENE_DIR / "top-view.png",
    "camera_map": SCENE_DIR / "camera-map.png",
    "shot_guides": {
        "r001": SCENE_DIR / "shot-guides" / "r001_camera.png",
        "r002": SCENE_DIR / "shot-guides" / "r002_camera.png",
        "r003": SCENE_DIR / "shot-guides" / "r003_camera.png",
        "r004": SCENE_DIR / "shot-guides" / "r004_camera.png",
    },
    "depth": {
        "r001": SCENE_DIR / "depth" / "r001_depth.png",
        "r002": SCENE_DIR / "depth" / "r002_depth.png",
        "r003": SCENE_DIR / "depth" / "r003_depth.png",
        "r004": SCENE_DIR / "depth" / "r004_depth.png",
    },
    "lineart": {
        "r001": SCENE_DIR / "lineart" / "r001_lineart.png",
        "r002": SCENE_DIR / "lineart" / "r002_lineart.png",
        "r003": SCENE_DIR / "lineart" / "r003_lineart.png",
        "r004": SCENE_DIR / "lineart" / "r004_lineart.png",
    },
    "manifest": SCENE_DIR / "blockout-export-manifest.json",
}

CAMERAS = {
    "r001": {
        "name": "CAM_R001_EXTERIOR_WIDE",
        "position": (0.0, -68.0, 2.2),
        "target": (0.0, -1.8, 5.4),
        "focal_length": 28,
    },
    "r002": {
        "name": "CAM_R002_EXTERIOR_CLOSER_IMPACT",
        "position": (0.0, -32.0, 3.1),
        "target": (0.0, -2.5, 4.1),
        "focal_length": 35,
    },
    "r003": {
        "name": "CAM_R003_GATEHOUSE_AFTERSHOCK",
        "position": (-7.2, 5.15, 11.15),
        "target": (-4.55, 6.75, 11.65),
        "focal_length": 35,
    },
    "r004": {
        "name": "CAM_R004_XUE_REAR_THREE_QUARTER",
        "position": (-1.4, 5.2, 11.75),
        "target": (1.6, -0.8, 10.95),
        "focal_length": 50,
    },
}

MATERIALS = {
    "blackstone": (0.045, 0.055, 0.065, 1.0),
    "dark_wall": (0.018, 0.020, 0.024, 1.0),
    "snow": (0.80, 0.88, 0.92, 1.0),
    "old_wood": (0.21, 0.13, 0.08, 1.0),
    "old_iron": (0.16, 0.17, 0.17, 1.0),
    "bone": (0.68, 0.62, 0.50, 1.0),
    "flag": (0.06, 0.06, 0.07, 1.0),
    "suming_wing": (0.86, 0.84, 0.77, 1.0),
    "beast": (0.18, 0.12, 0.08, 1.0),
    "human": (0.32, 0.34, 0.34, 1.0),
    "xue": (0.42, 0.43, 0.40, 1.0),
    "spear": (0.12, 0.12, 0.12, 1.0),
    "camera_marker": (0.85, 0.18, 0.10, 1.0),
    "attack_arrow": (0.72, 0.08, 0.05, 1.0),
    "guide_blue": (0.10, 0.32, 0.80, 1.0),
    "depth_white": (1.0, 1.0, 1.0, 1.0),
}


def ensure_dirs() -> None:
    for value in OUTPUTS.values():
        if isinstance(value, dict):
            for path in value.values():
                path.parent.mkdir(parents=True, exist_ok=True)
        else:
            value.parent.mkdir(parents=True, exist_ok=True)


def reset_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    scene = bpy.context.scene
    try:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 720
    scene.render.fps = 24
    scene.view_settings.view_transform = "Filmic"
    scene.view_settings.look = "Medium High Contrast"
    scene.world = bpy.data.worlds.new("SC001_WORLD") if not scene.world else scene.world
    scene.world.color = (0.025, 0.032, 0.040)


def mat(name: str):
    material = bpy.data.materials.new(name)
    material.diffuse_color = MATERIALS[name]
    return material


def create_materials():
    return {name: mat(name) for name in MATERIALS}


def cube(name: str, center, size, material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    return obj


def cylinder(name: str, center, radius: float, depth: float, material, vertices: int = 32) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    return obj


def cone(name: str, center, radius1: float, radius2: float, depth: float, material, vertices: int = 32) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius1, radius2=radius2, depth=depth, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    return obj


def line(name: str, start, end, material, bevel_depth: float = 0.035) -> bpy.types.Object:
    curve = bpy.data.curves.new(name, type="CURVE")
    curve.dimensions = "3D"
    curve.bevel_depth = bevel_depth
    spl = curve.splines.new("POLY")
    spl.points.add(1)
    spl.points[0].co = (start[0], start[1], start[2], 1.0)
    spl.points[1].co = (end[0], end[1], end[2], 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def add_label(name: str, text: str, location, size: float, material) -> bpy.types.Object:
    bpy.ops.object.text_add(location=location, rotation=(math.radians(90), 0, 0))
    obj = bpy.context.object
    obj.name = name
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.materials.append(material)
    return obj


def look_at(obj: bpy.types.Object, target) -> None:
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_camera(ref: str, spec: dict, materials: dict) -> bpy.types.Object:
    bpy.ops.object.camera_add(location=spec["position"])
    camera = bpy.context.object
    camera.name = spec["name"]
    camera.data.lens = spec["focal_length"]
    camera.data.sensor_fit = "HORIZONTAL"
    camera.data.dof.use_dof = False
    look_at(camera, spec["target"])
    cube(f"{ref}_camera_marker", spec["position"], (1.1, 1.1, 1.1), materials["camera_marker"])
    line(f"{ref}_camera_ray", spec["position"], spec["target"], materials["camera_marker"], 0.04)
    add_label(f"{ref}_label", ref.upper(), (spec["position"][0], spec["position"][1], 0.18), 1.3, materials["camera_marker"])
    return camera


def build_scene(materials: dict) -> dict[str, bpy.types.Object]:
    objects = {}

    # Ground and wall architecture.
    cube("snow_ground_exterior", (0, -42, -0.04), (72, 96, 0.08), materials["snow"])
    cube("snow_ground_interior", (0, 9, -0.04), (72, 26, 0.08), materials["snow"])
    cube("blackstone_outer_wall", (0, 0, 5), (72, 5, 10), materials["blackstone"])
    cube("central_old_wood_gate", (0, -2.9, 3.6), (7.6, 0.45, 7.0), materials["old_wood"])
    cube("gate_iron_crossbar", (0, -3.18, 3.25), (8.2, 0.22, 0.35), materials["old_iron"])
    cube("exterior_parapet", (0, -2.35, 11.0), (72, 0.8, 2.0), materials["dark_wall"])
    cube("gatehouse_side_parapet", (0, 2.35, 11.0), (72, 0.8, 2.0), materials["dark_wall"])
    cube("wall_walkway", (0, 0.1, 10.23), (70, 4.2, 0.24), materials["blackstone"])

    # Gatehouse body and timber frame.
    cube("upper_gatehouse_floor", (0, 5.25, 10.2), (14, 7.5, 0.28), materials["old_wood"])
    cube("upper_gatehouse_back_wall", (0, 8.9, 13.25), (14, 0.35, 6.1), materials["blackstone"])
    cube("upper_gatehouse_left_wall", (-7.0, 5.25, 13.25), (0.35, 7.5, 6.1), materials["blackstone"])
    cube("upper_gatehouse_right_wall", (7.0, 5.25, 13.25), (0.35, 7.5, 6.1), materials["blackstone"])
    cube("upper_gatehouse_roof", (0, 5.25, 16.8), (15, 8.2, 0.45), materials["old_wood"])
    for x in (-6.4, 6.4):
        for y in (2.0, 8.6):
            cube(f"gatehouse_post_{x}_{y}", (x, y, 13.1), (0.35, 0.35, 5.8), materials["old_wood"])
    cube("gatehouse_front_beam", (0, 2.0, 15.35), (14, 0.35, 0.35), materials["old_wood"])
    cube("gatehouse_back_beam", (0, 8.6, 15.35), (14, 0.35, 0.35), materials["old_wood"])

    # Bell frame and bone bell.
    for x in (-5.9, -3.7):
        for y in (4.75, 6.65):
            cube(f"bell_frame_post_{x}_{y}", (x, y, 12.7), (0.22, 0.22, 4.9), materials["old_wood"])
    cube("bell_frame_top_beam", (-4.8, 5.7, 15.4), (2.6, 2.2, 0.22), materials["old_wood"])
    line("bone_bell_chain", (-4.8, 5.7, 15.25), (-4.8, 5.7, 13.9), materials["old_iron"], 0.025)
    cone("same_bone_bell", (-4.8, 5.7, 13.2), 0.85, 0.45, 1.35, materials["bone"])

    # Flags and faction marks. The light wing stripe is a low-poly stand-in
    # for the P017 black-sun white-wing flag language.
    for side, x in (("left", -18), ("right", 18)):
        cube(f"{side}_suming_flag_pole", (x, -2.8, 12.3), (0.12, 0.12, 4.2), materials["old_iron"])
        cube(f"{side}_suming_black_flag", (x + (0.75 if x < 0 else -0.75), -3.05, 12.8), (1.5, 0.08, 1.1), materials["flag"])
        cube(f"{side}_suming_white_wing_mark", (x + (0.75 if x < 0 else -0.75), -3.12, 12.9), (0.95, 0.06, 0.16), materials["suming_wing"])

    # Siege beam, beast silhouettes, defenders and spear line.
    line("attack_direction_arrow_main", (0, -86, 0.3), (0, -4, 0.3), materials["attack_arrow"], 0.10)
    add_label("attack_direction_label", "BEAST ATTACK +Y", (0, -55, 0.18), 1.4, materials["attack_arrow"])
    line("siege_beam_or_mammoth_horn", (0, -23, 2.7), (0, -3.3, 3.2), materials["old_wood"], 0.25)
    for i, x in enumerate((-14, -9, -4, 5, 10, 15)):
        cube(f"beast_silhouette_{i}", (x, -38 - i * 2.5, 1.1), (1.6, 2.4, 2.2), materials["beast"])
    for i, x in enumerate(range(-28, 29, 7)):
        line(f"defender_spear_{i}", (x, -1.2, 10.7), (x + 0.8, -5.0, 12.0), materials["old_iron"], 0.025)
        cube(f"defender_silhouette_{i}", (x, -0.7, 10.75), (0.42, 0.42, 0.9), materials["human"])

    # Character blocks and props.
    cube("young_wall_soldier_half_collapsed", (-4.2, 7.4, 10.9), (0.8, 1.0, 0.9), materials["human"])
    line("young_soldier_dropped_spear", (-2.6, 5.2, 10.35), (-6.3, 7.9, 10.35), materials["spear"], 0.045)
    cube("xue_linqiang_body", (2.2, 0.6, 11.2), (0.8, 0.7, 1.5), materials["xue"])
    line("xue_hand_to_parapet", (2.0, 0.25, 11.25), (1.85, -2.05, 10.95), materials["xue"], 0.06)

    # Shot identity labels in top view.
    add_label("gate_label", "ONE GATE", (0, -4.4, 0.18), 1.2, materials["guide_blue"])
    add_label("bell_label", "SAME BONE BELL", (-4.8, 5.7, 10.52), 0.75, materials["guide_blue"])
    add_label("xue_label", "XUE", (2.2, 0.6, 10.55), 0.65, materials["guide_blue"])
    add_label("soldier_label", "YOUNG SOLDIER", (-4.2, 7.4, 10.55), 0.65, materials["guide_blue"])

    return objects


def setup_lighting() -> None:
    bpy.ops.object.light_add(type="SUN", location=(-18, -28, 24))
    sun = bpy.context.object
    sun.name = "cold_storm_break_sun"
    sun.data.energy = 3.0
    sun.rotation_euler = (math.radians(48), 0, math.radians(-22))
    bpy.ops.object.light_add(type="POINT", location=(0, -5, 4.0))
    impact = bpy.context.object
    impact.name = "cold_gate_impact_snow_blast"
    impact.data.energy = 900
    impact.data.color = (0.72, 0.84, 1.0)
    bpy.ops.object.light_add(type="POINT", location=(-10, -14, 2.0))
    fire = bpy.context.object
    fire.name = "low_dark_red_fire_edge"
    fire.data.energy = 260
    fire.data.color = (0.72, 0.18, 0.08)


def setup_cameras(materials: dict) -> dict[str, bpy.types.Object]:
    cameras = {}
    for ref, spec in CAMERAS.items():
        cameras[ref] = add_camera(ref, spec, materials)
    bpy.ops.object.camera_add(location=(0, -8, 88), rotation=(0, 0, 0))
    top = bpy.context.object
    top.name = "CAM_TOP_VIEW"
    top.data.type = "ORTHO"
    top.data.ortho_scale = 108
    look_at(top, (0, -8, 0))
    cameras["top"] = top
    return cameras


def render_still(camera: bpy.types.Object, filepath: Path, *, freestyle: bool = False) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.filepath = str(filepath)
    scene.render.use_freestyle = freestyle
    bpy.ops.render.render(write_still=True)


def render_depth(camera: bpy.types.Object, filepath: Path) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.use_freestyle = False
    scene.use_nodes = True
    tree = scene.node_tree
    tree.nodes.clear()
    render_layers = tree.nodes.new(type="CompositorNodeRLayers")
    normalize = tree.nodes.new(type="CompositorNodeNormalize")
    invert = tree.nodes.new(type="CompositorNodeInvert")
    output = tree.nodes.new(type="CompositorNodeOutputFile")
    output.base_path = str(filepath.parent)
    output.file_slots[0].path = filepath.stem + "_"
    output.format.file_format = "PNG"
    output.format.color_mode = "BW"
    tree.links.new(render_layers.outputs["Depth"], normalize.inputs[0])
    tree.links.new(normalize.outputs[0], invert.inputs[1])
    tree.links.new(invert.outputs[0], output.inputs[0])
    bpy.ops.render.render(write_still=False)
    produced = filepath.parent / f"{filepath.stem}_0001.png"
    if produced.exists():
        if filepath.exists():
            filepath.unlink()
        shutil.move(str(produced), str(filepath))
    scene.use_nodes = False


def export_all(cameras: dict[str, bpy.types.Object]) -> list[dict]:
    records = []
    render_still(cameras["top"], OUTPUTS["top_view"])
    records.append({"path": str(OUTPUTS["top_view"].relative_to(REPO_ROOT)), "status": "ready"})
    render_still(cameras["top"], OUTPUTS["camera_map"])
    records.append({"path": str(OUTPUTS["camera_map"].relative_to(REPO_ROOT)), "status": "ready"})

    for ref in ("r001", "r002", "r003", "r004"):
        render_still(cameras[ref], OUTPUTS["shot_guides"][ref])
        records.append({"path": str(OUTPUTS["shot_guides"][ref].relative_to(REPO_ROOT)), "status": "ready"})
        render_depth(cameras[ref], OUTPUTS["depth"][ref])
        records.append({"path": str(OUTPUTS["depth"][ref].relative_to(REPO_ROOT)), "status": "ready"})
        render_still(cameras[ref], OUTPUTS["lineart"][ref], freestyle=True)
        records.append({"path": str(OUTPUTS["lineart"][ref].relative_to(REPO_ROOT)), "status": "ready"})
    return records


def write_manifest(status: str, records: list[dict], error: str | None = None) -> None:
    payload = {
        "version": "sc001-blockout-export-manifest-v1",
        "project": "severed-homeland",
        "episode_id": "01",
        "scene_id": "SC001",
        "tool": "Blender Python",
        "script": str((SCENE_DIR / "build_sc001_blockout.py").relative_to(REPO_ROOT)),
        "layout": str((SCENE_DIR / "layout.yaml").relative_to(REPO_ROOT)),
        "status": status,
        "error": error,
        "outputs": records,
    }
    OUTPUTS["manifest"].write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()
    records: list[dict] = []
    try:
        reset_scene()
        materials = create_materials()
        build_scene(materials)
        setup_lighting()
        cameras = setup_cameras(materials)
        bpy.ops.wm.save_as_mainfile(filepath=str(OUTPUTS["blend"]))
        records.append({"path": str(OUTPUTS["blend"].relative_to(REPO_ROOT)), "status": "ready"})
        records.extend(export_all(cameras))
        write_manifest("ready", records)
    except Exception as exc:
        write_manifest("failed", records, error=repr(exc))
        raise


if __name__ == "__main__":
    main()
