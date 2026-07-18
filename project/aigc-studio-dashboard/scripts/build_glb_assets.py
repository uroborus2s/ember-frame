from __future__ import annotations

import math
import random
from pathlib import Path

import bpy


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "public" / "assets" / "3d"
TEXTURE_DIR = ROOT / "public" / "assets" / "textures"


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for data in (bpy.data.meshes, bpy.data.materials, bpy.data.images):
        for item in list(data):
            data.remove(item)


def rgb(hex_color: str, alpha: float = 1) -> tuple[float, float, float, float]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4)) + (alpha,)


def b_loc(loc):
    x, y, z = loc
    return (x, -z, y)


def b_scale(scale):
    x, y, z = scale
    return (x, z, y)


def b_rot(rot):
    return (0, 0, rot[1])


def make_image(name: str, width: int, height: int, pixel_fn):
    TEXTURE_DIR.mkdir(parents=True, exist_ok=True)
    image = bpy.data.images.new(name, width, height, alpha=True)
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.extend(pixel_fn(x, y))
    image.pixels.foreach_set(pixels)
    image.filepath_raw = str(TEXTURE_DIR / f"{name}.png")
    image.file_format = "PNG"
    image.save()
    return image


def make_textures():
    rng = random.Random(7)

    def wood(x, y):
        grain = math.sin(y * 0.19 + math.sin(x * 0.04) * 2.4) * 0.045 + rng.random() * 0.025
        return (0.69 + grain, 0.48 + grain * 0.65, 0.28 + grain * 0.35, 1)

    def floor(x, y):
        grout = x % 64 < 2 or y % 64 < 2
        shade = 0.76 + math.sin((x + y) * 0.035) * 0.018
        if grout:
            shade -= 0.08
        return (shade, shade, shade * 0.94, 1)

    def screen(x, y):
        grid = x % 32 < 2 or y % 24 < 2
        glow = 0.22 + 0.32 * math.sin(x * 0.06) * math.sin(y * 0.04)
        if grid:
            return (0.18, 0.62, 0.78, 1)
        return (0.04, 0.14 + glow * 0.25, 0.22 + glow * 0.5, 1)

    return {
        "wood": make_image("wood-grain", 256, 256, wood),
        "floor": make_image("stone-floor", 256, 256, floor),
        "screen": make_image("screen-ui", 256, 160, screen),
    }


def material(name: str, color="#ffffff", roughness=0.72, metalness=0, alpha=1, texture=None, emission=None, strength=0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = rgb(color, alpha)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metalness
        bsdf.inputs["Alpha"].default_value = alpha
        if emission and "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = rgb(emission)
            bsdf.inputs["Emission Strength"].default_value = strength
        if texture:
            tex = mat.node_tree.nodes.new("ShaderNodeTexImage")
            tex.image = texture
            mat.node_tree.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    if alpha < 1:
        mat.blend_method = "BLEND"
        mat.use_screen_refraction = True
        mat.show_transparent_back = True
    return mat


def bevel(obj, width=0.025, segments=2):
    if width <= 0:
        return obj
    bpy.context.view_layer.objects.active = obj
    mod = obj.modifiers.new("soft_edges", "BEVEL")
    mod.width = width
    mod.segments = segments
    bpy.ops.object.modifier_apply(modifier=mod.name)
    normal = obj.modifiers.new("weighted_normals", "WEIGHTED_NORMAL")
    bpy.ops.object.modifier_apply(modifier=normal.name)
    return obj


def cube(name, loc, scale, mat, rot=(0, 0, 0), parent=None, edge=0.025):
    bpy.ops.mesh.primitive_cube_add(size=1, location=b_loc(loc), rotation=b_rot(rot))
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = b_scale(scale)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    obj.parent = parent
    return bevel(obj, edge)


def cylinder(name, loc, radius, depth, mat, rot=(0, 0, 0), parent=None, vertices=32):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=b_loc(loc), rotation=b_rot(rot))
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    obj.parent = parent
    return bevel(obj, 0.01, 1)


def sphere(name, loc, radius, mat, scale=(1, 1, 1), parent=None):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, radius=radius, location=b_loc(loc))
    obj = bpy.context.object
    obj.name = name
    obj.scale = b_scale(scale)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    obj.parent = parent
    bpy.ops.object.shade_smooth()
    return obj


def empty(name, loc, rot_y=0, parent=None):
    obj = bpy.data.objects.new(name, None)
    obj.empty_display_type = "PLAIN_AXES"
    obj.empty_display_size = 0.22
    obj.location = b_loc(loc)
    obj.rotation_euler = (0, 0, rot_y)
    obj.parent = parent
    bpy.context.collection.objects.link(obj)
    return obj


def make_desk(name, x, z, mats, parent, width=1.7, depth=0.78):
    group = empty(name, (x, 0, z), parent=parent)
    cube(f"{name}_top", (0, 0.74, 0), (width, 0.12, depth), mats["wood"], parent=group, edge=0.035)
    for sx in (-1, 1):
        for sz in (-1, 1):
            cube(f"{name}_leg_{sx}_{sz}", (sx * (width / 2 - 0.13), 0.36, sz * (depth / 2 - 0.13)), (0.1, 0.68, 0.1), mats["darkWood"], parent=group)
    cube(f"{name}_monitor", (0.24, 1.05, 0.09), (0.72, 0.44, 0.06), mats["monitor"], parent=group, edge=0.02)
    cube(f"{name}_screen", (0.24, 1.05, 0.125), (0.64, 0.35, 0.012), mats["screen"], parent=group, edge=0.006)
    cube(f"{name}_keyboard", (-0.27, 0.82, 0.18), (0.56, 0.035, 0.18), mats["keyboard"], parent=group, edge=0.008)
    cube(f"{name}_tablet", (-0.3, 0.825, -0.16), (0.34, 0.025, 0.16), mats["monitor"], parent=group, edge=0.01)
    cylinder(f"{name}_lamp", (-0.65, 0.99, -0.22), 0.025, 0.42, mats["metal"], parent=group)
    cube(f"{name}_lamp_head", (-0.65, 1.19, -0.12), (0.26, 0.06, 0.12), mats["warmLight"], parent=group, edge=0.02)


def make_chair(name, x, z, rot_y, mats, parent):
    group = empty(name, (x, 0, z), rot_y, parent=parent)
    cube(f"{name}_seat", (0, 0.38, 0), (0.58, 0.11, 0.52), mats["chair"], parent=group, edge=0.045)
    cube(f"{name}_back", (0, 0.78, -0.27), (0.58, 0.72, 0.1), mats["chair"], parent=group, edge=0.045)
    for lx in (-0.2, 0.2):
        cube(f"{name}_leg_{lx}", (lx, 0.18, 0.16), (0.075, 0.36, 0.075), mats["black"], parent=group)
    cylinder(f"{name}_base", (0, 0.12, 0.02), 0.25, 0.035, mats["metal"], parent=group)


def make_plant(name, x, z, scale, mats, parent):
    group = empty(name, (x, 0, z), parent=parent)
    cylinder(f"{name}_pot", (0, 0.18 * scale, 0), 0.17 * scale, 0.36 * scale, mats["pot"], parent=group)
    for i in range(9):
        leaf = cube(f"{name}_leaf_{i}", (0, 0.52 * scale, 0.16 * scale), (0.07 * scale, 0.018 * scale, 0.52 * scale), mats["plant"], parent=group, edge=0.004)
        leaf.rotation_euler = (0.55, 0, i / 9 * math.tau)


def build_office():
    clear_scene()
    textures = make_textures()
    mats = {
        "floor": material("stone_floor_material", texture=textures["floor"], roughness=0.82),
        "wall": material("warm_white_wall", "#eef0eb", roughness=0.76),
        "glass": material("soft_blue_glass", "#9ed8e4", roughness=0.05, alpha=0.34),
        "wood": material("wood_table_material", texture=textures["wood"], roughness=0.58),
        "darkWood": material("dark_wood", "#795031", roughness=0.65),
        "chair": material("charcoal_chair", "#34383b", roughness=0.64),
        "metal": material("brushed_metal", "#70797c", roughness=0.38, metalness=0.35),
        "black": material("soft_black", "#1e2529", roughness=0.55),
        "monitor": material("monitor_black", "#172129", roughness=0.3),
        "screen": material("blue_screen_texture", texture=textures["screen"], roughness=0.28, emission="#5bc5ff", strength=0.45),
        "keyboard": material("keyboard_dark", "#2d363b", roughness=0.5),
        "plant": material("plant_green", "#4d8951", roughness=0.78),
        "pot": material("ceramic_pot", "#9a7758", roughness=0.72),
        "warmLight": material("warm_light_panel", "#ffe4a1", roughness=0.3, emission="#ffd57a", strength=0.5),
        "sun": material("painted_sun_patch", "#fff1a7", roughness=0.9, alpha=0.22),
    }
    root = empty("office", (0, 0, 0))

    cube("floor", (0, -0.03, 0), (10.8, 0.06, 7.2), mats["floor"], parent=root, edge=0)
    cube("back_wall", (0, 1.4, -3.6), (10.8, 2.8, 0.12), mats["wall"], parent=root)
    cube("left_wall", (-5.4, 1.4, 0), (0.12, 2.8, 7.2), mats["wall"], parent=root)
    cube("front_half_wall", (0.6, 0.68, 3.55), (7.4, 1.35, 0.12), mats["wall"], parent=root)
    cube("glass_wall", (5.35, 1.05, -0.8), (0.1, 1.7, 3.8), mats["glass"], parent=root)

    for x in (-3.6, -2.1, -0.6, 0.9):
        cube(f"sun_window_{x}", (x, 1.55, -3.515), (1.1, 1.05, 0.04), mats["glass"], parent=root, edge=0.01)
    for x in (-2.7, 0.4, 2.4):
        patch = cube(f"sun_patch_{x}", (x, 0.025, 1.2), (0.9, 0.012, 3.2), mats["sun"], rot=(0, -0.62, 0), parent=root, edge=0)

    for name, x, z in (
        ("desk_back_a", -3.2, -2.18),
        ("desk_back_b", -1.2, -2.18),
        ("desk_back_c", 0.8, -2.18),
        ("desk_front_a", 1.1, 1.45),
        ("desk_front_b", 3.15, 1.45),
    ):
        make_desk(name, x, z, mats, root)
    make_desk("desk_curved_main", 0.92, 1.2, mats, root, width=2.55, depth=0.95)
    cube("meeting_table", (-2.5, 0.76, 1.55), (2.55, 0.12, 0.98), mats["wood"], parent=root, edge=0.045)

    for name, x, z, rot in (
        ("chair_back_a", -3.2, -2.85, 0),
        ("chair_back_b", -1.2, -2.85, 0),
        ("chair_back_c", 0.8, -2.85, 0),
        ("chair_front_b", 3.15, 0.72, 0),
        ("chair_meet_a", -3.0, 0.86, 0),
        ("chair_meet_b", -2.0, 2.22, math.pi),
        ("chair_main", 0.92, 0.68, 0),
    ):
        make_chair(name, x, z, rot, mats, root)

    for name, x, z in (("rack_a", 3.7, -2.65), ("rack_b", 4.35, -2.55), ("rack_c", 4.7, -1.85)):
        cube(name, (x, 0.78, z), (0.45, 1.55, 0.42), mats["monitor"], parent=root)
        for y in (0.6, 0.84, 1.1, 1.32):
            cube(f"{name}_led_{y}", (x, y, z + 0.22), (0.34, 0.025, 0.025), mats["screen"], parent=root, edge=0.004)

    for args in (("plant_left", -4.7, 2.55, 1.1), ("plant_right", 4.65, 2.35, 0.9), ("plant_server", 2.75, -2.95, 0.75), ("plant_meeting", -2.5, 1.55, 0.42)):
        make_plant(*args, mats, root)

    for name, x, z, rot in (
        ("seat_back_a", -3.2, -2.67, 0),
        ("seat_back_b", -1.2, -2.67, 0),
        ("seat_back_c", 0.8, -2.67, 0),
        ("seat_front_b", 3.15, 0.9, 0),
        ("seat_meet_a", -3.0, 1.04, 0),
        ("seat_meet_b", -2.0, 2.04, math.pi),
        ("seat_main", 0.92, 0.86, 0),
        ("walk_main_a", -3.7, 1.9, 0),
        ("walk_main_b", -1.4, 1.55, 0),
        ("walk_main_c", 0.5, 1.0, 0),
        ("walker_a", 3.9, 2.45, 0),
        ("walker_b", 2.3, 2.3, 0),
        ("walker_c", 1.1, 2.0, 0),
    ):
        empty(name, (x, 0, z), rot, root)

    bpy.ops.object.light_add(type="SUN", location=(-4.5, 8.2, 5.8))
    bpy.context.object.name = "office_sun"
    bpy.context.object.data.energy = 2.2
    bpy.context.object.parent = root

    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(ASSET_DIR / "office.glb"), export_format="GLB")


def build_character():
    clear_scene()
    skin = material("warm_skin", "#efb28b", roughness=0.68)
    shirt = material("navy_blazer", "#24415f", roughness=0.64)
    pants = material("office_pants", "#263746", roughness=0.68)
    hair_mat = material("black_hair", "#151719", roughness=0.55)
    white = material("shirt_white", "#f3eee5", roughness=0.7)
    eye = material("soft_eye", "#101417", roughness=0.45)
    shoe = material("white_sneaker", "#f4f0e8", roughness=0.62)
    badge = material("id_badge", "#f4d47b", roughness=0.5)

    root = empty("character", (0, 0, 0))
    body = cube("body", (0, 1.02, 0), (0.4, 0.58, 0.22), shirt, parent=root, edge=0.08)
    cube("shirt_front", (0, 1.04, 0.117), (0.18, 0.42, 0.018), white, parent=body, edge=0.006)
    cube("id_badge", (0.09, 0.94, 0.135), (0.07, 0.095, 0.012), badge, parent=body, edge=0.003)

    head = sphere("head", (0, 1.43, 0), 0.2, skin, scale=(0.92, 1.05, 0.88), parent=root)
    hair = sphere("hair", (0, 1.52, -0.02), 0.215, hair_mat, scale=(1.02, 0.64, 0.95), parent=root)
    sphere("leftEye", (-0.07, 1.46, 0.18), 0.025, eye, parent=root)
    sphere("rightEye", (0.07, 1.46, 0.18), 0.025, eye, parent=root)
    cube("mouth", (0, 1.38, 0.18), (0.08, 0.012, 0.008), material("mouth_warm", "#9d4d45"), parent=head, edge=0.002)

    cube("leftArm", (-0.3, 1.0, 0), (0.1, 0.5, 0.09), shirt, parent=root, edge=0.05)
    cube("rightArm", (0.3, 1.0, 0), (0.1, 0.5, 0.09), shirt, parent=root, edge=0.05)
    cube("leftHand", (-0.3, 0.72, 0.02), (0.11, 0.1, 0.09), skin, parent=root, edge=0.04)
    cube("rightHand", (0.3, 0.72, 0.02), (0.11, 0.1, 0.09), skin, parent=root, edge=0.04)
    cube("skirt", (0, 0.68, 0), (0.44, 0.28, 0.27), pants, parent=root, edge=0.04)
    cube("leftThigh", (-0.11, 0.55, 0), (0.13, 0.46, 0.13), pants, parent=root, edge=0.05)
    cube("rightThigh", (0.11, 0.55, 0), (0.13, 0.46, 0.13), pants, parent=root, edge=0.05)
    cube("leftShin", (-0.11, 0.22, 0), (0.12, 0.48, 0.12), pants, parent=root, edge=0.045)
    cube("rightShin", (0.11, 0.22, 0), (0.12, 0.48, 0.12), pants, parent=root, edge=0.045)
    cube("leftShoe", (-0.11, 0.04, 0.07), (0.16, 0.08, 0.26), shoe, parent=root, edge=0.035)
    cube("rightShoe", (0.11, 0.04, 0.07), (0.16, 0.08, 0.26), shoe, parent=root, edge=0.035)

    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(ASSET_DIR / "character.glb"), export_format="GLB")


build_office()
build_character()
print(f"wrote {ASSET_DIR / 'office.glb'}")
print(f"wrote {ASSET_DIR / 'character.glb'}")
