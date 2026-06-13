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
EPISODE_DIR = SCENE_DIR.parents[2]
SCENE_ASSET_DIR = EPISODE_DIR / "assets" / "director-room" / "scenes" / "SC001"
OUTPUTS = {
    "blend": SCENE_DIR / "blockout.blend",
    "top_view": SCENE_DIR / "top-view.png",
    "camera_map": SCENE_DIR / "camera-map.png",
    "scene_assets": {
        "master_reference_front": SCENE_ASSET_DIR / "master-reference-front.png",
        "master_reference_reverse": SCENE_ASSET_DIR / "master-reference-reverse.png",
        "key_prop_placement": SCENE_ASSET_DIR / "key-prop-placement.png",
        "blocking_overview": SCENE_ASSET_DIR / "blocking-overview.png",
    },
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
    "material_lock": SCENE_ASSET_DIR / "material-lock.json",
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
        "position": (1.8, 2.3, 12.0),
        "target": (-4.6, 6.3, 12.2),
        "focal_length": 22,
    },
    "r004": {
        "name": "CAM_R004_XUE_REAR_THREE_QUARTER",
        "position": (-2.4, 3.4, 13.0),
        "target": (2.1, -0.8, 12.0),
        "focal_length": 30,
    },
}

MASTER_CAMERAS = {
    "master_front": {
        "name": "CAM_MASTER_FRONT_TEXTURED_EXTERIOR",
        "position": (0.0, -58.0, 7.2),
        "target": (0.0, -1.8, 7.0),
        "focal_length": 38,
    },
    "master_reverse": {
        "name": "CAM_MASTER_REVERSE_CITYSIDE",
        "position": (20.0, 18.5, 13.5),
        "target": (0.0, 5.3, 12.3),
        "focal_length": 34,
    },
    "key_prop": {
        "name": "CAM_KEY_PROP_BELL_GATEHOUSE",
        "position": (6.8, 1.0, 14.4),
        "target": (-3.9, 5.8, 12.9),
        "focal_length": 34,
    },
}

MATERIALS = {
    "blackstone": (0.24, 0.29, 0.34, 1.0),
    "dark_wall": (0.16, 0.18, 0.21, 1.0),
    "stone_joint": (0.055, 0.065, 0.075, 1.0),
    "stone_chip": (0.08, 0.10, 0.12, 1.0),
    "snow": (0.80, 0.88, 0.92, 1.0),
    "snow_edge": (0.92, 0.97, 1.0, 1.0),
    "impact_snow": (0.72, 0.86, 0.94, 1.0),
    "old_wood": (0.42, 0.25, 0.12, 1.0),
    "wood_dark": (0.20, 0.12, 0.07, 1.0),
    "wood_light": (0.54, 0.35, 0.18, 1.0),
    "old_iron": (0.38, 0.39, 0.39, 1.0),
    "iron_dark": (0.12, 0.13, 0.13, 1.0),
    "ancient_bell_metal": (0.18, 0.16, 0.13, 1.0),
    "zhaoming_emblem_remnant": (0.55, 0.42, 0.22, 1.0),
    "flag": (0.12, 0.12, 0.14, 1.0),
    "suming_wing": (0.86, 0.84, 0.77, 1.0),
    "beast": (0.42, 0.22, 0.10, 1.0),
    "human": (0.52, 0.58, 0.62, 1.0),
    "xue": (0.72, 0.75, 0.68, 1.0),
    "spear": (0.28, 0.28, 0.28, 1.0),
    "city_shadow": (0.10, 0.13, 0.16, 1.0),
    "window_warm": (0.95, 0.55, 0.17, 1.0),
    "smoke": (0.32, 0.36, 0.38, 1.0),
    "camera_marker": (1.0, 0.08, 0.02, 1.0),
    "attack_arrow": (1.0, 0.02, 0.00, 1.0),
    "guide_blue": (0.02, 0.20, 1.0, 1.0),
    "overview_wall": (0.04, 0.05, 0.06, 1.0),
    "overview_gate": (0.10, 0.62, 1.0, 1.0),
    "overview_gatehouse": (0.58, 0.22, 0.78, 1.0),
    "overview_bell": (1.0, 0.82, 0.12, 1.0),
    "overview_xue": (0.12, 0.82, 0.30, 1.0),
    "overview_soldier": (0.08, 0.70, 0.88, 1.0),
    "overview_flag": (0.02, 0.02, 0.02, 1.0),
    "depth_white": (1.0, 1.0, 1.0, 1.0),
}

TEXTURE_NOISE = {
    "blackstone": {"scale": 28, "detail": 9, "dark": 0.72, "light": 1.24},
    "dark_wall": {"scale": 22, "detail": 7, "dark": 0.65, "light": 1.12},
    "old_wood": {"scale": 18, "detail": 8, "dark": 0.70, "light": 1.35},
    "ancient_bell_metal": {"scale": 18, "detail": 7, "dark": 0.72, "light": 1.16},
    "snow": {"scale": 34, "detail": 3, "dark": 0.92, "light": 1.08},
    "city_shadow": {"scale": 14, "detail": 4, "dark": 0.80, "light": 1.15},
}

MATERIAL_LOCK = {
    "version": "sc001-material-lock-v1",
    "project": "severed-homeland",
    "episode_id": "01",
    "scene_id": "SC001",
    "principle": "All master references, shot guides, depth maps, and lineart exports are rendered from one Blender scene using the same locked material IDs and procedural texture/detail geometry.",
    "city_backplate_policy": "A low-detail city silhouette exists only for cityside reverse master continuity. When R003/R004 face outside from the gatehouse or wall-top, the exterior view must be battlefield snow haze, smoke, attackers and siege pressure only: no houses, warm windows, streets, city towers, second wall or second gate.",
    "materials": {
        "blackstone": "main wall, parapets, gatehouse stone, procedural stone noise",
        "stone_joint": "dark mortar seams laid onto the wall and gatehouse back wall",
        "stone_chip": "chipped blackstone patches and cracks",
        "snow_edge": "locked snow caps and wind streaks on ledges",
        "old_wood": "gate, gatehouse floor, roof, posts, and bell frame",
        "wood_dark": "plank seams, grain cuts, and weathering grooves",
        "old_iron": "gate straps, rivets, chains, spear metal, flag poles, old bell hardware",
        "ancient_bell_metal": "five-thousand-year-old Zhaoming old-empire metal alarm bell body; oxidized dark bronze/iron, cracks, dents, missing rim chips, old repairs",
        "zhaoming_emblem_remnant": "broken unreadable fragments of the Zhaoming sun-moon astrolabe emblem on the bell; never a complete clean crest",
        "flag": "P017 black banner base",
        "suming_wing": "P017 white wing marks",
        "city_shadow": "distant city silhouette backplate",
        "window_warm": "small locked city window accents",
    },
    "shot_usage_lock": {
        "r001_r002": "front wall, central old wood gate, impact beam, flags, stone/snow/gate material layers",
        "r003": "same gatehouse floor, dropped spear, young soldier knocked down alive by aftershock, ancient metal alarm bell swinging, bell frame, no houses/city outside",
        "r004": "same gatehouse/parapet, Xue position, ancient metal alarm bell background, exterior battlefield snow haze only with no houses/city",
    },
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
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0
    scene.view_settings.gamma = 1
    scene.world = bpy.data.worlds.new("SC001_WORLD") if not scene.world else scene.world
    scene.world.color = (0.42, 0.46, 0.50)


def scaled_color(color, factor: float) -> tuple[float, float, float, float]:
    return (
        max(0.0, min(1.0, color[0] * factor)),
        max(0.0, min(1.0, color[1] * factor)),
        max(0.0, min(1.0, color[2] * factor)),
        color[3],
    )


def mat(name: str):
    material = bpy.data.materials.new(name)
    color = MATERIALS[name]
    material.diffuse_color = color
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    emission = nodes.new(type="ShaderNodeEmission")
    if name in TEXTURE_NOISE:
        noise_config = TEXTURE_NOISE[name]
        noise = nodes.new(type="ShaderNodeTexNoise")
        noise.inputs["Scale"].default_value = noise_config["scale"]
        noise.inputs["Detail"].default_value = noise_config["detail"]
        ramp = nodes.new(type="ShaderNodeValToRGB")
        ramp.color_ramp.elements[0].position = 0.22
        ramp.color_ramp.elements[0].color = scaled_color(color, noise_config["dark"])
        ramp.color_ramp.elements[1].position = 1.0
        ramp.color_ramp.elements[1].color = scaled_color(color, noise_config["light"])
        material.node_tree.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
        material.node_tree.links.new(ramp.outputs["Color"], emission.inputs["Color"])
    else:
        emission.inputs["Color"].default_value = color
    emission.inputs["Strength"].default_value = 0.9
    output = nodes.new(type="ShaderNodeOutputMaterial")
    material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
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


def sphere(name: str, center, radius: float, material, segments: int = 16) -> bpy.types.Object:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=8, radius=radius, location=center)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    return obj


def torus(name: str, center, major_radius: float, minor_radius: float, material) -> bpy.types.Object:
    bpy.ops.mesh.primitive_torus_add(
        major_segments=40,
        minor_segments=8,
        major_radius=major_radius,
        minor_radius=minor_radius,
        location=center,
    )
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
    bpy.ops.object.text_add(location=location, rotation=(0, 0, 0))
    obj = bpy.context.object
    obj.name = name
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.materials.append(material)
    return obj


def mark_helpers(objects, helper_name: str) -> None:
    for obj in objects:
        obj[helper_name] = True


def overview_cube(name: str, center, size, material) -> bpy.types.Object:
    obj = cube(name, center, size, material)
    obj["overview_helper"] = True
    return obj


def overview_label(name: str, text: str, location, size: float, material) -> bpy.types.Object:
    obj = add_label(name, text, location, size, material)
    obj["overview_helper"] = True
    return obj


def overview_line(name: str, start, end, material, bevel_depth: float = 0.12) -> bpy.types.Object:
    obj = line(name, start, end, material, bevel_depth)
    obj["overview_helper"] = True
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
    marker = cube(f"{ref}_camera_marker", (spec["position"][0], spec["position"][1], 18.8), (2.2, 2.2, 0.35), materials["camera_marker"])
    ray = line(
        f"{ref}_camera_ray",
        (spec["position"][0], spec["position"][1], 18.7),
        (spec["target"][0], spec["target"][1], 18.7),
        materials["camera_marker"],
        0.12,
    )
    label_positions = {
        "r001": (-9.0, -67.0, 19.0),
        "r002": (8.5, -34.5, 19.0),
        "r003": (-18.0, 10.8, 19.0),
        "r004": (18.0, 10.8, 19.0),
    }
    label_sizes = {
        "r001": 2.6,
        "r002": 2.6,
        "r003": 2.2,
        "r004": 2.2,
    }
    label = add_label(f"{ref}_label", ref.upper(), label_positions[ref], label_sizes[ref], materials["camera_marker"])
    mark_helpers((marker, ray, label), "camera_map_helper")
    return camera


def add_plain_camera(spec: dict) -> bpy.types.Object:
    bpy.ops.object.camera_add(location=spec["position"])
    camera = bpy.context.object
    camera.name = spec["name"]
    camera.data.lens = spec["focal_length"]
    camera.data.sensor_fit = "HORIZONTAL"
    camera.data.dof.use_dof = False
    look_at(camera, spec["target"])
    return camera


def add_wall_material_detail(materials: dict) -> None:
    front_y = -2.58
    rear_y = 2.58
    for idx, z in enumerate((1.15, 2.35, 3.55, 4.75, 5.95, 7.15, 8.35, 9.55)):
        cube(f"front_wall_horizontal_mortar_{idx}", (0, front_y, z), (71.0, 0.07, 0.055), materials["stone_joint"])
        cube(f"rear_wall_horizontal_mortar_{idx}", (0, rear_y, z), (71.0, 0.07, 0.055), materials["stone_joint"])

    for row_idx, z in enumerate((0.65, 1.85, 3.05, 4.25, 5.45, 6.65, 7.85, 9.05)):
        offset = 0 if row_idx % 2 == 0 else 3
        for col_idx, x in enumerate(range(-33 + offset, 34, 6)):
            if -5.0 < x < 5.0 and z < 8.4:
                continue
            cube(
                f"front_wall_vertical_mortar_{row_idx}_{col_idx}",
                (x, front_y - 0.015, z),
                (0.055, 0.09, 0.95),
                materials["stone_joint"],
            )

    chip_specs = [
        (-31, -2.62, 6.7, 1.2, 0.10, 0.42),
        (-24, -2.62, 2.2, 0.9, 0.10, 0.36),
        (-17, -2.62, 8.4, 1.5, 0.10, 0.50),
        (-10, -2.62, 4.6, 0.8, 0.10, 0.30),
        (11, -2.62, 5.9, 1.1, 0.10, 0.44),
        (19, -2.62, 3.1, 1.4, 0.10, 0.38),
        (27, -2.62, 7.3, 1.0, 0.10, 0.42),
        (33, -2.62, 1.8, 0.7, 0.10, 0.26),
    ]
    for idx, (x, y, z, sx, sy, sz) in enumerate(chip_specs):
        cube(f"front_wall_blackstone_chip_{idx}", (x, y, z), (sx, sy, sz), materials["stone_chip"])

    for idx, x in enumerate((-33, -27, -21, -15, -8, 8, 15, 22, 29, 34)):
        cube(
            f"front_wall_snow_wind_streak_{idx}",
            (x, -2.66, 10.05 - (idx % 3) * 0.45),
            (0.38, 0.09, 1.05 + (idx % 2) * 0.5),
            materials["snow_edge"],
        )
    cube("front_parapet_snow_cap_locked", (0, -2.88, 12.05), (72.0, 0.7, 0.18), materials["snow_edge"])
    cube("rear_parapet_snow_cap_locked", (0, 2.88, 12.05), (72.0, 0.7, 0.18), materials["snow_edge"])


def add_gate_material_detail(materials: dict) -> None:
    for idx, x in enumerate((-3.1, -1.55, 0.0, 1.55, 3.1)):
        cube(f"gate_vertical_plank_seam_{idx}", (x, -3.34, 3.6), (0.06, 0.11, 6.8), materials["wood_dark"])
    for idx, z in enumerate((1.15, 2.05, 4.95, 6.05)):
        cube(f"gate_horizontal_plank_cut_{idx}", (0, -3.35, z), (7.4, 0.10, 0.07), materials["wood_dark"])
    for idx, z in enumerate((2.15, 5.15)):
        cube(f"gate_iron_band_textured_{idx}", (0, -3.42, z), (8.3, 0.14, 0.22), materials["iron_dark"])
        for rivet_idx, x in enumerate((-3.45, -2.25, -1.05, 1.05, 2.25, 3.45)):
            cube(
                f"gate_iron_rivet_{idx}_{rivet_idx}",
                (x, -3.52, z),
                (0.18, 0.09, 0.18),
                materials["old_iron"],
            )
    for idx, x in enumerate((-2.7, -0.8, 1.15, 2.95)):
        line(
            f"gate_wood_grain_crack_{idx}",
            (x, -3.56, 0.7 + idx * 0.55),
            (x + 0.55, -3.56, 2.2 + idx * 0.74),
            materials["wood_light"],
            0.025,
        )

    for idx, (x, z, radius) in enumerate(((-1.8, 2.9, 0.7), (1.7, 3.2, 0.55), (0.0, 4.0, 0.85))):
        sphere(f"gate_impact_snow_puff_{idx}", (x, -4.1 - idx * 0.18, z), radius, materials["impact_snow"], segments=12)


def add_gatehouse_material_detail(materials: dict) -> None:
    for idx, x in enumerate((-5.25, -3.5, -1.75, 0.0, 1.75, 3.5, 5.25)):
        cube(f"gatehouse_floor_plank_seam_{idx}", (x, 5.25, 10.38), (0.05, 7.25, 0.06), materials["wood_dark"])
    for idx, y in enumerate((2.6, 3.7, 4.8, 5.9, 7.0, 8.1)):
        cube(f"gatehouse_roof_plank_shadow_{idx}", (0, y, 16.52), (14.4, 0.06, 0.08), materials["wood_dark"])
    for idx, z in enumerate((11.7, 13.0, 14.3)):
        cube(f"gatehouse_back_wall_mortar_{idx}", (0, 8.68, z), (13.2, 0.06, 0.05), materials["stone_joint"])
    for idx, x in enumerate((-5.4, -2.7, 0.0, 2.7, 5.4)):
        cube(f"gatehouse_back_wall_vertical_mortar_{idx}", (x, 8.65, 13.2), (0.05, 0.08, 5.0), materials["stone_joint"])

    cube("gatehouse_roof_snow_cap", (0, 5.25, 17.08), (15.2, 8.35, 0.18), materials["snow_edge"])
    cube("gatehouse_front_beam_snow_lip", (0, 1.78, 15.72), (13.8, 0.24, 0.12), materials["snow_edge"])
    cube("gatehouse_back_beam_snow_lip", (0, 8.82, 15.72), (13.8, 0.24, 0.12), materials["snow_edge"])


def add_alarm_bell_material_detail(materials: dict) -> None:
    for idx, (z, radius) in enumerate(((12.72, 0.72), (13.14, 0.62), (13.55, 0.48))):
        torus(f"alarm_bell_ring_band_{idx}", (-4.8, 5.7, z), radius, 0.035, materials["zhaoming_emblem_remnant"])
    scratch_specs = [
        ((-5.22, 5.13, 13.68), (-5.36, 5.07, 12.75)),
        ((-4.38, 5.18, 13.58), (-4.25, 5.10, 12.92)),
        ((-5.05, 6.32, 13.42), (-5.22, 6.40, 12.72)),
        ((-4.52, 6.30, 13.55), (-4.42, 6.38, 12.88)),
    ]
    for idx, (start, end) in enumerate(scratch_specs):
        line(f"alarm_bell_crack_{idx}", start, end, materials["zhaoming_emblem_remnant"], 0.025)


def add_flag_material_detail(materials: dict) -> None:
    flag_specs = [
        ("left", -17.25, -3.18),
        ("right", 18.75, -3.18),
    ]
    for side, x, y in flag_specs:
        line(f"{side}_flag_wing_diagonal_top", (x - 0.55, y, 13.12), (x + 0.55, y, 12.72), materials["suming_wing"], 0.035)
        line(f"{side}_flag_wing_diagonal_low", (x - 0.45, y, 12.68), (x + 0.38, y, 12.48), materials["suming_wing"], 0.028)
        cube(f"{side}_flag_torn_lower_edge", (x, y, 12.24), (1.35, 0.05, 0.08), materials["stone_joint"])


def add_city_backplate(materials: dict) -> None:
    cube("city_backplate_low_wall", (0, 20.2, 2.3), (62.0, 0.75, 4.6), materials["city_shadow"])
    tower_specs = [
        (-30, 20.1, 4.9, 4.0, 0.8, 9.8),
        (-21, 20.1, 5.9, 3.3, 0.8, 11.8),
        (-12, 20.1, 4.4, 4.7, 0.8, 8.8),
        (-3, 20.1, 6.4, 3.6, 0.8, 12.8),
        (8, 20.1, 5.2, 4.2, 0.8, 10.4),
        (18, 20.1, 6.0, 3.5, 0.8, 12.0),
        (29, 20.1, 4.7, 4.8, 0.8, 9.4),
    ]
    for idx, (x, y, z, sx, sy, sz) in enumerate(tower_specs):
        cube(f"city_silhouette_tower_{idx}", (x, y, z), (sx, sy, sz), materials["city_shadow"])
        for win_idx, wz in enumerate((z + sz * 0.08, z + sz * 0.22, z + sz * 0.36)):
            if win_idx == 1 and idx % 2:
                continue
            cube(f"city_window_{idx}_{win_idx}", (x + sx * 0.18, y - 0.43, wz), (0.28, 0.06, 0.22), materials["window_warm"])
    for idx, x in enumerate((-25, -7, 12, 25)):
        sphere(f"city_smoke_column_base_{idx}", (x, 19.5, 10.0 + idx * 0.45), 0.72, materials["smoke"], segments=12)
        sphere(f"city_smoke_column_top_{idx}", (x + 0.8, 19.6, 11.4 + idx * 0.45), 0.95, materials["smoke"], segments=12)


def add_master_material_detail_layer(materials: dict) -> None:
    add_wall_material_detail(materials)
    add_gate_material_detail(materials)
    add_gatehouse_material_detail(materials)
    add_alarm_bell_material_detail(materials)
    add_flag_material_detail(materials)
    add_city_backplate(materials)


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

    # Bell frame and ancient Zhaoming metal alarm bell.
    for x in (-5.9, -3.7):
        for y in (4.75, 6.65):
            cube(f"bell_frame_post_{x}_{y}", (x, y, 12.7), (0.22, 0.22, 4.9), materials["old_wood"])
    cube("bell_frame_top_beam", (-4.8, 5.7, 15.4), (2.6, 2.2, 0.22), materials["old_wood"])
    line("alarm_bell_chain", (-4.8, 5.7, 15.25), (-4.8, 5.7, 13.9), materials["old_iron"], 0.025)
    cone("same_ancient_zhaoming_metal_alarm_bell", (-4.8, 5.7, 13.2), 0.85, 0.45, 1.35, materials["ancient_bell_metal"])

    # Flags and faction marks. The light wing stripe is a low-poly stand-in
    # for the P017 black-sun white-wing flag language.
    for side, x in (("left", -18), ("right", 18)):
        cube(f"{side}_suming_flag_pole", (x, -2.8, 12.3), (0.12, 0.12, 4.2), materials["old_iron"])
        cube(f"{side}_suming_black_flag", (x + (0.75 if x < 0 else -0.75), -3.05, 12.8), (1.5, 0.08, 1.1), materials["flag"])
        cube(f"{side}_suming_white_wing_mark", (x + (0.75 if x < 0 else -0.75), -3.12, 12.9), (0.95, 0.06, 0.16), materials["suming_wing"])

    # Siege beam, beast silhouettes, defenders and spear line.
    attack_arrow = line("attack_direction_arrow_main", (0, -86, 0.3), (0, -4, 0.3), materials["attack_arrow"], 0.10)
    attack_label = add_label("attack_direction_label", "BEAST ATTACK +Y", (0, -55, 0.18), 1.4, materials["attack_arrow"])
    attack_arrow["camera_map_helper"] = True
    attack_label["camera_map_helper"] = True
    line("siege_beam_or_mammoth_horn", (0, -23, 2.7), (0, -3.3, 3.2), materials["old_wood"], 0.25)
    for i, x in enumerate((-14, -9, -4, 5, 10, 15)):
        cube(f"beast_silhouette_{i}", (x, -38 - i * 2.5, 1.1), (1.6, 2.4, 2.2), materials["beast"])
    for i, x in enumerate(range(-28, 29, 7)):
        line(f"defender_spear_{i}", (x, -1.2, 10.7), (x + 0.8, -5.0, 12.0), materials["old_iron"], 0.025)
        cube(f"defender_silhouette_{i}", (x, -0.7, 10.75), (0.42, 0.42, 0.9), materials["human"])

    # Character blocks and props.
    cube("young_wall_soldier_half_collapsed", (-4.2, 7.2, 12.25), (1.1, 1.1, 1.8), materials["human"])
    line("young_soldier_dropped_spear", (-2.6, 5.2, 10.35), (-6.3, 7.9, 10.35), materials["spear"], 0.045)
    cube("xue_linqiang_body", (2.2, 0.0, 12.1), (0.9, 0.75, 2.0), materials["xue"])
    line("xue_hand_to_parapet", (2.0, 0.1, 12.15), (1.85, -2.05, 10.95), materials["xue"], 0.06)

    add_master_material_detail_layer(materials)

    # Shot identity labels in top view.
    overview_z = 18.35
    overview_items = [
        overview_cube("overview_blackstone_wall_band", (0, 0, overview_z), (72, 5.8, 0.28), materials["overview_wall"]),
        overview_cube("overview_gate_blue_lock", (0, -2.9, overview_z + 0.16), (9.0, 1.8, 0.32), materials["overview_gate"]),
        overview_cube("overview_gatehouse_zone", (0, 5.25, overview_z + 0.08), (16.0, 8.8, 0.24), materials["overview_gatehouse"]),
        overview_cube("overview_left_flag", (-18, -3.1, overview_z + 0.28), (2.4, 1.0, 0.32), materials["overview_flag"]),
        overview_cube("overview_right_flag", (18, -3.1, overview_z + 0.28), (2.4, 1.0, 0.32), materials["overview_flag"]),
        overview_cube("overview_xue_marker", (2.2, 0.6, overview_z + 0.5), (2.4, 2.0, 0.45), materials["overview_xue"]),
        overview_cube("overview_young_soldier_marker", (-4.2, 7.2, overview_z + 0.5), (2.4, 2.0, 0.45), materials["overview_soldier"]),
        overview_line("overview_attack_axis_red", (0, -86, overview_z + 0.55), (0, -4.4, overview_z + 0.55), materials["attack_arrow"], 0.18),
        overview_line("overview_gate_impact_tick", (-4.8, -4.4, overview_z + 0.65), (4.8, -4.4, overview_z + 0.65), materials["attack_arrow"], 0.12),
        overview_label("overview_scene_title", "SC001 ONE WALL / ONE GATE", (0, 17.0, overview_z + 0.7), 2.0, materials["guide_blue"]),
        overview_label("overview_wall_label", "BLACKSTONE WALL", (-24, 0, overview_z + 0.7), 1.8, materials["suming_wing"]),
        overview_label("overview_gate_label", "GATE", (0, -7.0, overview_z + 0.7), 2.0, materials["guide_blue"]),
        overview_label("overview_gatehouse_label", "GATEHOUSE", (0, 11.2, overview_z + 0.7), 1.45, materials["suming_wing"]),
        overview_label("overview_attack_label", "BEAST ATTACK ->", (-12.5, -46, overview_z + 0.7), 2.0, materials["attack_arrow"]),
        overview_label("overview_xue_label", "XUE", (6.2, 1.3, overview_z + 0.7), 1.5, materials["overview_xue"]),
        overview_label("overview_soldier_label", "YOUNG SOLDIER", (-12.0, 8.2, overview_z + 0.7), 1.35, materials["overview_soldier"]),
        overview_label("overview_flag_label", "P017 FLAGS", (22, -5.8, overview_z + 0.7), 1.45, materials["suming_wing"]),
    ]
    bell_marker = cylinder("overview_alarm_bell_marker", (-4.8, 5.7, overview_z + 0.75), 1.35, 0.42, materials["overview_bell"], vertices=32)
    bell_marker["overview_helper"] = True
    overview_items.append(bell_marker)
    overview_items.append(overview_label("overview_bell_label", "BONE BELL", (-10.8, 4.8, overview_z + 0.9), 1.35, materials["overview_bell"]))
    for obj in overview_items:
        obj.hide_render = True

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
    for ref, spec in MASTER_CAMERAS.items():
        cameras[ref] = add_plain_camera(spec)
    bpy.ops.object.camera_add(location=(0, -28, 88), rotation=(0, 0, 0))
    top = bpy.context.object
    top.name = "CAM_TOP_VIEW"
    top.data.type = "ORTHO"
    top.data.ortho_scale = 145
    look_at(top, (0, -28, 0))
    cameras["top"] = top
    return cameras


def render_still(camera: bpy.types.Object, filepath: Path, *, freestyle: bool = False) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.filepath = str(filepath)
    scene.render.use_freestyle = freestyle
    bpy.ops.render.render(write_still=True)


def set_camera_map_helpers_visible(visible: bool) -> None:
    for obj in bpy.context.scene.objects:
        if obj.get("camera_map_helper"):
            obj.hide_render = not visible


def set_overview_helpers_visible(visible: bool) -> None:
    for obj in bpy.context.scene.objects:
        if obj.get("overview_helper"):
            obj.hide_render = not visible


def write_material_lock() -> dict:
    OUTPUTS["material_lock"].write_text(
        json.dumps(MATERIAL_LOCK, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {"path": str(OUTPUTS["material_lock"].relative_to(REPO_ROOT)), "status": "ready"}


def render_depth(camera: bpy.types.Object, filepath: Path) -> None:
    scene = bpy.context.scene
    scene.camera = camera
    scene.render.use_freestyle = False
    renderable = [
        obj
        for obj in bpy.context.scene.objects
        if obj.type in {"MESH", "CURVE", "FONT"} and not obj.hide_render
    ]
    camera_forward = camera.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))
    depths = [
        max(0.0, (obj.location - camera.location).dot(camera_forward))
        for obj in renderable
    ]
    near = min(depths) if depths else 0.0
    far = max(depths) if depths else 1.0
    span = max(far - near, 0.001)
    original_materials = {
        obj.name: [slot.material for slot in obj.material_slots]
        for obj in renderable
    }
    original_world_color = tuple(scene.world.color)
    depth_materials = []
    try:
        for obj, depth in zip(renderable, depths):
            shade = 1.0 - max(0.0, min(1.0, (depth - near) / span))
            material = bpy.data.materials.new(f"depth_{obj.name}")
            material.diffuse_color = (shade, shade, shade, 1.0)
            material.use_nodes = True
            nodes = material.node_tree.nodes
            nodes.clear()
            emission = nodes.new(type="ShaderNodeEmission")
            emission.inputs["Color"].default_value = (shade, shade, shade, 1.0)
            emission.inputs["Strength"].default_value = 1.0
            output = nodes.new(type="ShaderNodeOutputMaterial")
            material.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
            depth_materials.append(material)
            obj.data.materials.clear()
            obj.data.materials.append(material)
        scene.world.color = (0.0, 0.0, 0.0)
        scene.render.filepath = str(filepath)
        bpy.ops.render.render(write_still=True)
    finally:
        for obj in renderable:
            obj.data.materials.clear()
            for material in original_materials.get(obj.name, []):
                if material is not None:
                    obj.data.materials.append(material)
        for material in depth_materials:
            bpy.data.materials.remove(material, do_unlink=True)
        scene.world.color = original_world_color


def export_all(cameras: dict[str, bpy.types.Object]) -> list[dict]:
    records = []
    set_camera_map_helpers_visible(False)
    set_overview_helpers_visible(True)
    render_still(cameras["top"], OUTPUTS["top_view"])
    records.append({"path": str(OUTPUTS["top_view"].relative_to(REPO_ROOT)), "status": "ready"})
    set_camera_map_helpers_visible(True)
    set_overview_helpers_visible(True)
    render_still(cameras["top"], OUTPUTS["camera_map"])
    records.append({"path": str(OUTPUTS["camera_map"].relative_to(REPO_ROOT)), "status": "ready"})

    set_camera_map_helpers_visible(False)
    set_overview_helpers_visible(False)
    scene_asset_pairs = [
        ("master_front", "master_reference_front"),
        ("master_reverse", "master_reference_reverse"),
        ("key_prop", "key_prop_placement"),
    ]
    for camera_key, output_key in scene_asset_pairs:
        render_still(cameras[camera_key], OUTPUTS["scene_assets"][output_key])
        records.append({"path": str(OUTPUTS["scene_assets"][output_key].relative_to(REPO_ROOT)), "status": "ready"})
    set_camera_map_helpers_visible(True)
    set_overview_helpers_visible(True)
    render_still(cameras["top"], OUTPUTS["scene_assets"]["blocking_overview"])
    records.append({"path": str(OUTPUTS["scene_assets"]["blocking_overview"].relative_to(REPO_ROOT)), "status": "ready"})

    set_camera_map_helpers_visible(False)
    set_overview_helpers_visible(False)
    for ref in ("r001", "r002", "r003", "r004"):
        render_still(cameras[ref], OUTPUTS["shot_guides"][ref])
        records.append({"path": str(OUTPUTS["shot_guides"][ref].relative_to(REPO_ROOT)), "status": "ready"})
        render_depth(cameras[ref], OUTPUTS["depth"][ref])
        records.append({"path": str(OUTPUTS["depth"][ref].relative_to(REPO_ROOT)), "status": "ready"})
        render_still(cameras[ref], OUTPUTS["lineart"][ref], freestyle=True)
        records.append({"path": str(OUTPUTS["lineart"][ref].relative_to(REPO_ROOT)), "status": "ready"})
    set_camera_map_helpers_visible(True)
    set_overview_helpers_visible(True)
    return records


def write_manifest(status: str, records: list[dict], error: str | None = None) -> None:
    payload = {
        "version": "sc001-blockout-export-manifest-v2",
        "project": "severed-homeland",
        "episode_id": "01",
        "scene_id": "SC001",
        "tool": "Blender Python",
        "script": str((SCENE_DIR / "build_sc001_blockout.py").relative_to(REPO_ROOT)),
        "layout": str((SCENE_DIR / "layout.yaml").relative_to(REPO_ROOT)),
        "material_lock": str(OUTPUTS["material_lock"].relative_to(REPO_ROOT)),
        "scene_asset_dir": str(SCENE_ASSET_DIR.relative_to(REPO_ROOT)),
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
        bpy.context.preferences.filepaths.save_version = 0
        materials = create_materials()
        build_scene(materials)
        setup_lighting()
        cameras = setup_cameras(materials)
        records.append(write_material_lock())
        bpy.ops.wm.save_as_mainfile(filepath=str(OUTPUTS["blend"]))
        records.append({"path": str(OUTPUTS["blend"].relative_to(REPO_ROOT)), "status": "ready"})
        records.extend(export_all(cameras))
        write_manifest("ready", records)
    except Exception as exc:
        write_manifest("failed", records, error=repr(exc))
        raise


if __name__ == "__main__":
    main()
