from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "assets" / "25d"
CHAR_DIR = OUT / "characters"
VENDOR = ROOT / "public" / "assets" / "vendor" / "polyhaven"
WIDTH = 1536
HEIGHT = 900


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def rgba(hex_color, alpha=1):
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4)) + (alpha,)


def mat(name, color, roughness=0.7, metallic=0, alpha=1, emission=None, strength=0):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = rgba(color, alpha)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Alpha"].default_value = alpha
        if emission and "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = rgba(emission)
            bsdf.inputs["Emission Strength"].default_value = strength
    if alpha < 1:
        material.blend_method = "BLEND"
        material.show_transparent_back = True
    return material


def noise_mat(name, color_a, color_b, scale=24, roughness=0.7, bump=0.025):
    material = mat(name, color_a, roughness)
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    bsdf = nodes.get("Principled BSDF")
    if not bsdf:
        return material
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = scale
    noise.inputs["Detail"].default_value = 10
    noise.inputs["Roughness"].default_value = 0.58
    ramp = nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.18
    ramp.color_ramp.elements[0].color = rgba(color_a)
    ramp.color_ramp.elements[1].position = 1
    ramp.color_ramp.elements[1].color = rgba(color_b)
    links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    if bump:
        bump_node = nodes.new("ShaderNodeBump")
        bump_node.inputs["Strength"].default_value = bump
        bump_node.inputs["Distance"].default_value = 0.08
        links.new(noise.outputs["Fac"], bump_node.inputs["Height"])
        links.new(bump_node.outputs["Normal"], bsdf.inputs["Normal"])
    return material


def tag(obj, layer):
    obj["render_layer"] = layer
    return obj


def bevel(obj, width=0.02, segments=2):
    if width <= 0:
        return obj
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    mod = obj.modifiers.new("soft_edges", "BEVEL")
    mod.width = width
    mod.segments = segments
    bpy.ops.object.modifier_apply(modifier=mod.name)
    normal = obj.modifiers.new("weighted_normals", "WEIGHTED_NORMAL")
    bpy.ops.object.modifier_apply(modifier=normal.name)
    obj.select_set(False)
    return obj


def cube(name, loc, scale, material, layer="base", rot=0, edge=0.025):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=(0, 0, rot))
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    return tag(bevel(obj, edge), layer)


def cyl(name, loc, radius, depth, material, layer="base", rot=(0, 0, 0), vertices=32, edge=0.005):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return tag(bevel(obj, edge, 1), layer)


def sphere(name, loc, radius, material, layer="base", scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=radius, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return tag(obj, layer)


def import_gltf(name, asset_id, loc, target=1.0, rot=0, layer="base"):
    path = VENDOR / asset_id / f"{asset_id}.gltf"
    if not path.exists():
        return []
    before = set(bpy.context.scene.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    imported = [obj for obj in bpy.context.scene.objects if obj not in before]
    meshes = [obj for obj in imported if obj.type == "MESH"]
    if not meshes:
        return imported
    min_v = Vector((1e9, 1e9, 1e9))
    max_v = Vector((-1e9, -1e9, -1e9))
    for obj in meshes:
        for corner in obj.bound_box:
            world = obj.matrix_world @ Vector(corner)
            min_v.x = min(min_v.x, world.x)
            min_v.y = min(min_v.y, world.y)
            min_v.z = min(min_v.z, world.z)
            max_v.x = max(max_v.x, world.x)
            max_v.y = max(max_v.y, world.y)
            max_v.z = max(max_v.z, world.z)
    center = (min_v + max_v) / 2
    size = max((max_v - min_v).x, (max_v - min_v).y, (max_v - min_v).z)
    scale = target / size if size else 1
    parent = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(parent)
    parent.location = loc
    parent.rotation_euler[2] = rot
    for obj in imported:
        obj.name = f"{name}_{obj.name}"
        obj.location = (obj.location - center) * scale
        obj.scale = obj.scale * scale
        obj.parent = parent
        if obj.type == "MESH":
            tag(obj, layer)
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            try:
                bpy.ops.object.shade_smooth()
            except Exception:
                pass
            obj.select_set(False)
    return imported + [parent]


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def setup_render():
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 96
    scene.cycles.use_denoising = True
    scene.render.resolution_x = WIDTH
    scene.render.resolution_y = HEIGHT
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "AgX"
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.view_settings.exposure = 0.15
    scene.view_settings.gamma = 1
    scene.world = bpy.data.worlds.new("soft_day_world")
    scene.world.color = (0.82, 0.9, 0.88)

    bpy.ops.object.light_add(type="SUN", location=(-6, -6, 8))
    sun = bpy.context.object
    sun.name = "warm_window_sun"
    sun.data.energy = 3.1
    sun.data.angle = math.radians(3.2)
    look_at(sun, (0, 0, 0))

    bpy.ops.object.light_add(type="AREA", location=(-5.2, -4.9, 4.8))
    area = bpy.context.object
    area.name = "large_window_softbox"
    area.data.energy = 920
    area.data.size = 7.2

    bpy.ops.object.light_add(type="AREA", location=(4.4, 2.0, 3.2))
    fill = bpy.context.object
    fill.name = "server_room_cool_fill"
    fill.data.energy = 190
    fill.data.size = 4.0

    bpy.ops.object.camera_add(location=(8.8, -9.8, 6.8))
    cam = bpy.context.object
    cam.name = "iso_camera"
    look_at(cam, (0.15, -0.05, 0.85))
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 10.8
    scene.camera = cam
    return cam


def make_mats():
    return {
        "floor": noise_mat("warm_stone_floor", "#bbb9ad", "#e0ded2", 42, 0.84, 0.018),
        "dark_floor": noise_mat("server_dark_floor", "#252d30", "#485255", 30, 0.78, 0.018),
        "grout": mat("fine_grout", "#aeb0a7", 0.9),
        "wall": noise_mat("sunlit_wall", "#e8e6db", "#f7f5ec", 18, 0.76, 0.01),
        "wall_panel": noise_mat("warm_wall_panel", "#cfc3ad", "#e5dcc8", 26, 0.66, 0.012),
        "wood": noise_mat("honey_oak", "#94602f", "#d7a15b", 34, 0.5, 0.035),
        "wood_dark": noise_mat("desk_edge_walnut", "#4b321f", "#875b35", 28, 0.6, 0.025),
        "leather": noise_mat("soft_charcoal_leather", "#2a2c2d", "#4e5252", 36, 0.52, 0.018),
        "metal": mat("brushed_aluminum", "#8f9798", 0.34, 0.25),
        "trim": mat("champagne_trim", "#d5b46f", 0.38, 0.35),
        "black": mat("soft_black_plastic", "#171d21", 0.5),
        "screen": mat("blue_screen_glow", "#5da9c7", 0.22, emission="#54c8ff", strength=0.55),
        "screen_dark": mat("dark_screen_glow", "#1c3d55", 0.28, emission="#2ba9ff", strength=0.8),
        "neon": mat("warm_neon_strip", "#ffc66c", 0.22, emission="#ffc66c", strength=1.25),
        "paper": mat("warm_paper", "#f3eddc", 0.85),
        "plant": mat("office_plant_green", "#477b4b", 0.72),
        "pot": mat("ceramic_planter", "#8d7158", 0.73),
        "glass": mat("blue_tinted_glass", "#9fd3de", 0.05, alpha=0.28),
        "shadow": mat("painted_shadow", "#1f2a2d", 0.95, alpha=0.18),
        "light": mat("warm_lamp_emission", "#ffe3a6", 0.28, emission="#ffd37a", strength=0.7),
    }


def make_room(m):
    cube("floor", (0, 0, -0.03), (10.8, 6.7, 0.06), m["floor"], edge=0)
    for x in [i * 0.9 - 5.4 for i in range(13)]:
        cube(f"tile_x_{x:.1f}", (x, 0, 0.003), (0.018, 6.7, 0.006), m["grout"], edge=0)
    for y in [i * 0.9 - 3.15 for i in range(8)]:
        cube(f"tile_y_{y:.1f}", (0, y, 0.004), (10.8, 0.018, 0.006), m["grout"], edge=0)

    cube("back_wall", (0, 3.32, 1.35), (10.8, 0.12, 2.7), m["wall"])
    cube("left_wall", (-5.4, 0, 1.35), (0.12, 6.7, 2.7), m["wall"])
    cube("front_half_wall", (0.8, -3.28, 0.46), (7.2, 0.14, 0.92), m["wall"], "foreground")
    cube("right_glass_panel", (5.35, -0.8, 1.0), (0.08, 3.8, 2.0), m["glass"], "glass")

    for x in (-3.6, -2.1, -0.6, 0.9):
        cube(f"window_{x}", (x, 3.255, 1.58), (1.1, 0.04, 1.05), m["glass"], "glass", edge=0.01)
    for x in (-4.4, -2.7, -1.0, 0.8, 2.6):
        cube(f"sun_patch_{x}", (x, -0.45, 0.012), (0.72, 4.25, 0.008), m["shadow"], "shadow", rot=0.55, edge=0)


def desk(name, x, y, m, width=1.72, depth=0.82, rot=0):
    cube(f"{name}_top", (x, y, 0.76), (width, depth, 0.12), m["wood"], rot=rot, edge=0.045)
    cube(f"{name}_gold_trim_front", (x, y - depth / 2 - 0.015, 0.835), (width, 0.025, 0.035), m["trim"], rot=rot, edge=0.006)
    cube(f"{name}_front_lip", (x, y - depth / 2 + 0.03, 0.64), (width, 0.08, 0.28), m["wood_dark"], "foreground", rot=rot, edge=0.02)
    for sx in (-1, 1):
        for sy in (-1, 1):
            cube(f"{name}_leg_{sx}_{sy}", (x + sx * (width / 2 - 0.15), y + sy * (depth / 2 - 0.15), 0.34), (0.1, 0.1, 0.68), m["wood_dark"], edge=0.015)
    cube(f"{name}_monitor", (x + 0.28, y + 0.04, 1.08), (0.72, 0.055, 0.44), m["black"], rot=rot, edge=0.018)
    cube(f"{name}_screen", (x + 0.28, y - 0.005, 1.08), (0.63, 0.012, 0.34), m["screen"], rot=rot, edge=0.004)
    cube(f"{name}_keyboard", (x - 0.25, y - 0.24, 0.84), (0.58, 0.18, 0.035), m["black"], rot=rot, edge=0.01)
    cube(f"{name}_mouse", (x + 0.22, y - 0.26, 0.845), (0.12, 0.08, 0.025), m["black"], rot=rot + 0.08, edge=0.018)
    cyl(f"{name}_coffee", (x + 0.53, y + 0.2, 0.89), 0.045, 0.11, m["paper"], vertices=28, edge=0.004)
    cube(f"{name}_paper_a", (x - 0.62, y + 0.08, 0.835), (0.28, 0.22, 0.01), m["paper"], rot=rot + 0.1, edge=0.004)
    cube(f"{name}_paper_b", (x + 0.68, y - 0.18, 0.835), (0.24, 0.18, 0.01), m["paper"], rot=rot - 0.15, edge=0.004)
    cyl(f"{name}_lamp_stem", (x - 0.7, y + 0.2, 1.02), 0.018, 0.42, m["metal"], rot=(0, 0.4, 0))
    cube(f"{name}_lamp_head", (x - 0.68, y + 0.08, 1.24), (0.28, 0.12, 0.06), m["light"], edge=0.02)


def chair(name, x, y, m, rot=0):
    cube(f"{name}_seat", (x, y, 0.4), (0.58, 0.52, 0.11), m["leather"], rot=rot, edge=0.05)
    cube(f"{name}_back", (x, y + 0.25, 0.82), (0.6, 0.1, 0.78), m["leather"], rot=rot, edge=0.05)
    cube(f"{name}_arm_l", (x - 0.35, y, 0.59), (0.06, 0.44, 0.06), m["metal"], rot=rot, edge=0.018)
    cube(f"{name}_arm_r", (x + 0.35, y, 0.59), (0.06, 0.44, 0.06), m["metal"], rot=rot, edge=0.018)
    cyl(f"{name}_post", (x, y, 0.22), 0.045, 0.34, m["metal"], edge=0.004)
    cyl(f"{name}_base", (x, y, 0.08), 0.26, 0.04, m["metal"], vertices=40)
    for i, ang in enumerate((0, 1.26, 2.52, 3.78, 5.04)):
        cube(f"{name}_caster_{i}", (x + math.cos(ang) * 0.26, y + math.sin(ang) * 0.26, 0.045), (0.08, 0.045, 0.04), m["black"], rot=ang, edge=0.012)


def plant(name, x, y, m, scale=1):
    cyl(f"{name}_pot", (x, y, 0.19 * scale), 0.18 * scale, 0.38 * scale, m["pot"])
    for i in range(9):
        leaf = cube(f"{name}_leaf_{i}", (x, y, 0.58 * scale), (0.07 * scale, 0.42 * scale, 0.025 * scale), m["plant"], edge=0.004)
        leaf.rotation_euler = (math.radians(22), 0, i / 9 * math.tau)


def shelves(name, x, y, m):
    cube(f"{name}_case", (x, y, 1.05), (0.75, 0.26, 1.8), m["wood_dark"], edge=0.025)
    for z in (0.48, 0.86, 1.24, 1.62):
        cube(f"{name}_shelf_{z}", (x, y - 0.02, z), (0.68, 0.22, 0.04), m["wood"], edge=0.01)
    for i in range(12):
        cube(f"{name}_book_{i}", (x - 0.29 + (i % 6) * 0.1, y - 0.1, 0.55 + (i // 6) * 0.72), (0.07, 0.08, 0.28), m["screen" if i % 4 == 0 else "paper"], edge=0.004)


def screen_wall(name, x, y, m, cols=3, rows=2, rot=0):
    cube(f"{name}_backplate", (x, y, 1.45), (1.65, 0.06, 0.98), m["black"], rot=rot, edge=0.02)
    for row in range(rows):
        for col in range(cols):
            cube(
                f"{name}_screen_{row}_{col}",
                (x - 0.5 + col * 0.5, y - 0.045, 1.22 + row * 0.35),
                (0.44, 0.016, 0.26),
                m["screen_dark"],
                rot=rot,
                edge=0.006,
            )


def curved_console(name, cx, y, m):
    for i, angle in enumerate((-32, -16, 0, 16, 32)):
        rad = math.radians(angle)
        x = cx + math.sin(rad) * 1.35
        yy = y + math.cos(rad) * 0.22
        rot = -rad * 0.7
        cube(f"{name}_desk_{i}", (x, yy, 0.76), (0.92, 0.62, 0.12), m["wood"], rot=rot, edge=0.04)
        cube(f"{name}_lip_{i}", (x, yy - 0.29, 0.64), (0.92, 0.07, 0.28), m["wood_dark"], "foreground", rot=rot, edge=0.02)
        cube(f"{name}_monitor_{i}", (x, yy - 0.02, 1.1), (0.58, 0.05, 0.38), m["black"], rot=rot, edge=0.018)
        cube(f"{name}_screen_{i}", (x, yy - 0.055, 1.1), (0.5, 0.012, 0.3), m["screen_dark"], rot=rot, edge=0.004)
        cube(f"{name}_keyboard_{i}", (x, yy - 0.24, 0.84), (0.44, 0.15, 0.035), m["black"], rot=rot, edge=0.008)
        cube(f"{name}_tablet_{i}", (x - 0.2, yy - 0.12, 0.86), (0.25, 0.16, 0.02), m["screen"], rot=rot + 0.05, edge=0.006)
    chair(f"{name}_chair", cx, y - 0.75, m)


def server_room(m):
    cube("server_room_floor", (3.9, 2.02, 0.012), (2.75, 1.85, 0.012), m["dark_floor"], edge=0)
    cube("server_room_back_wall", (3.9, 2.92, 1.1), (2.75, 0.1, 2.2), m["black"], edge=0.015)
    cube("server_glass_front", (3.9, 1.07, 1.08), (2.85, 0.07, 2.15), m["glass"], "glass", edge=0.01)
    for i, x in enumerate((3.0, 3.65, 4.3, 4.95)):
        cube(f"server_rack_{i}", (x, 2.25, 0.92), (0.42, 0.46, 1.65), m["black"], edge=0.025)
        for z in (0.45, 0.7, 0.95, 1.2, 1.45):
            cube(f"server_rack_{i}_led_{z}", (x, 2.01, z), (0.3, 0.022, 0.022), m["screen"], edge=0.003)
    for x in (2.65, 5.18):
        cube(f"server_neon_{x}", (x, 1.95, 1.86), (0.035, 1.45, 0.035), m["screen"], edge=0.006)


def stage_room(m):
    cube("stage_floor", (4.05, -2.32, 0.04), (2.15, 1.38, 0.08), m["wood_dark"], edge=0.025)
    cube("stage_back_panel", (4.05, -2.98, 1.12), (2.15, 0.08, 1.95), m["wall_panel"], edge=0.02)
    cube("stage_neon_left", (3.02, -3.03, 1.12), (0.04, 0.04, 1.72), m["neon"], edge=0.008)
    cube("stage_neon_right", (5.08, -3.03, 1.12), (0.04, 0.04, 1.72), m["neon"], edge=0.008)
    for i, x in enumerate((3.55, 4.55)):
        cyl(f"stage_lightstand_{i}", (x, -2.55, 0.72), 0.025, 1.35, m["black"], edge=0.004)
        cube(f"stage_light_{i}", (x, -2.55, 1.48), (0.28, 0.18, 0.18), m["black"], edge=0.02)
    cyl("stage_stool_a", (3.55, -1.88, 0.42), 0.23, 0.06, m["leather"], vertices=40)
    cyl("stage_stool_b", (4.65, -1.9, 0.42), 0.23, 0.06, m["leather"], vertices=40)


def build_office():
    m = make_mats()
    make_room(m)
    for name, x, y in (
        ("desk_a", -3.25, 1.8),
        ("desk_b", -1.25, 1.8),
        ("desk_c", 0.75, 1.8),
        ("desk_d", 2.85, -1.1),
        ("desk_e", 0.9, -1.1),
    ):
        desk(name, x, y, m)
    curved_console("director_console", -2.65, -1.05, m)
    cube("meeting_table", (2.6, 1.15, 0.76), (2.55, 1.02, 0.12), m["wood"], edge=0.045)
    cube("meeting_table_lip", (2.6, 0.66, 0.64), (2.55, 0.08, 0.28), m["wood_dark"], "foreground", edge=0.02)

    for name, x, y, rot in (
        ("chair_a", -3.25, 1.1, 0),
        ("chair_b", -1.25, 1.1, 0),
        ("chair_c", 0.75, 1.1, 0),
        ("chair_d", 2.85, -1.78, 0),
        ("chair_e", 0.9, -1.78, 0),
        ("chair_meet_a", 1.9, 0.55, 0),
        ("chair_meet_b", 2.9, 1.75, math.pi),
    ):
        chair(name, x, y, m, rot)

    for name, x, y, rot in (
        ("asset_chair_a", -3.25, 1.08, 0),
        ("asset_chair_b", -1.25, 1.08, 0),
        ("asset_chair_c", 0.75, 1.08, 0),
        ("asset_chair_d", 2.85, -1.8, 0),
        ("asset_chair_e", 0.9, -1.8, 0),
    ):
        import_gltf(name, "modern_arm_chair_01", (x, y, 0.18), 0.78, rot)

    server_room(m)
    stage_room(m)
    screen_wall("review_screen_wall", -4.2, -0.55, m, cols=3, rows=2)

    shelves("shelf_left", -4.75, 2.25, m)
    shelves("shelf_back", 2.7, 3.15, m)
    import_gltf("asset_drawer_a", "drawer_cabinet", (-4.85, -0.35, 0.08), 1.05, math.radians(90))
    import_gltf("asset_drawer_b", "drawer_cabinet", (4.95, -0.75, 0.08), 1.05, math.radians(-90))
    import_gltf("asset_lamp_console", "desk_lamp_arm_01", (-3.65, -0.92, 0.86), 0.62, math.radians(18))
    import_gltf("asset_notepad_a", "office_notepads", (-0.35, 1.55, 0.86), 0.42, math.radians(8))
    import_gltf("asset_notepad_b", "office_notepads", (2.2, 0.95, 0.84), 0.42, math.radians(-12))
    import_gltf("asset_coffee_table", "modern_coffee_table_02", (3.95, -1.88, 0.2), 1.05, math.radians(8))
    for args in (("plant_left", -4.65, -2.15, 1.1), ("plant_back", 4.6, 2.85, 0.9), ("plant_table", 2.6, 1.15, 0.45), ("plant_front", 1.55, -2.7, 0.75)):
        plant(args[0], args[1], args[2], m, args[3])
    import_gltf("asset_pachira_left", "pachira_aquatica_01", (-4.85, -2.15, 0.05), 1.15)
    import_gltf("asset_pachira_back", "pachira_aquatica_01", (4.82, 2.82, 0.05), 1.0)
    for i, x in enumerate((-3.8, -2.7, -1.6, 1.8, 2.7)):
        cube(f"wall_art_{i}", (x, 3.24, 1.6), (0.65, 0.04, 0.42), m["screen" if i % 2 else "paper"], edge=0.01)

    anchors = {
        "seat_a": (-3.25, 1.05, 0.55),
        "seat_b": (-1.25, 1.05, 0.55),
        "seat_c": (0.75, 1.05, 0.55),
        "seat_main": (-2.7, -1.88, 0.55),
        "seat_meet_a": (1.9, 0.52, 0.55),
        "seat_meet_b": (2.9, 1.78, 0.55),
        "walk_a": (0.2, -2.65, 0),
        "walk_b": (-1.25, -2.35, 0),
        "walk_c": (-2.35, -2.05, 0),
    }
    return anchors


def set_layers(visible_layers, transparent):
    bpy.context.scene.render.film_transparent = transparent
    for obj in bpy.context.scene.objects:
        if obj.type in {"CAMERA", "LIGHT"}:
            obj.hide_render = False
            continue
        obj.hide_render = obj.get("render_layer", "base") not in visible_layers


def render(path):
    bpy.context.scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def screen_anchor(cam, name, pos, width_pct=8.2, z=10):
    coord = world_to_camera_view(bpy.context.scene, cam, Vector(pos))
    return {
        "name": name,
        "x": round(coord.x * WIDTH, 1),
        "y": round((1 - coord.y) * HEIGHT, 1),
        "widthPct": width_pct,
        "z": z,
    }


def character_materials(female):
    return {
        "skin": mat("skin_female" if female else "skin_male", "#efb28b", 0.62),
        "hair": mat("hair_female" if female else "hair_male", "#2b1d18" if female else "#17191b", 0.52),
        "blazer": mat("blazer_female" if female else "blazer_male", "#294760" if female else "#20384f", 0.58),
        "shirt": mat("shirt", "#f4eee3", 0.7),
        "bottom": mat("skirt" if female else "pants", "#d3b184" if female else "#263747", 0.6),
        "shoe": mat("shoe", "#d6b890" if female else "#f2f0e8", 0.58),
        "eye": mat("eye", "#101417", 0.35),
        "badge": mat("badge", "#f1cc6b", 0.45),
    }


def make_character(name, female=True):
    m = character_materials(female)
    parts = {}
    parts["body"] = cube(f"{name}_body", (0, 0, 1.03), (0.42, 0.24, 0.58), m["blazer"], "character", edge=0.08)
    cube(f"{name}_shirt", (0, -0.13, 1.06), (0.2, 0.02, 0.42), m["shirt"], "character", edge=0.004)
    cube(f"{name}_badge", (0.1, -0.145, 0.98), (0.07, 0.012, 0.09), m["badge"], "character", edge=0.003)
    parts["head"] = sphere(f"{name}_head", (0, -0.02, 1.48), 0.22, m["skin"], "character", scale=(0.92, 0.9, 1.06))
    parts["hair"] = sphere(f"{name}_hair", (0, 0.02, 1.58), 0.23, m["hair"], "character", scale=(1.02, 0.88, 0.68))
    if female:
        cyl(f"{name}_hair_back", (0, 0.13, 1.34), 0.1, 0.62, m["hair"], "character", vertices=32)
    sphere(f"{name}_eye_l", (-0.07, -0.21, 1.5), 0.025, m["eye"], "character")
    sphere(f"{name}_eye_r", (0.07, -0.21, 1.5), 0.025, m["eye"], "character")
    cube(f"{name}_mouth", (0, -0.225, 1.39), (0.08, 0.01, 0.012), mat(f"{name}_mouth_mat", "#9d4d45"), "character", edge=0.002)
    parts["arm_l"] = cyl(f"{name}_arm_l", (-0.31, -0.02, 0.98), 0.05, 0.5, m["blazer"], "character", vertices=24)
    parts["arm_r"] = cyl(f"{name}_arm_r", (0.31, -0.02, 0.98), 0.05, 0.5, m["blazer"], "character", vertices=24)
    parts["hand_l"] = sphere(f"{name}_hand_l", (-0.31, -0.03, 0.7), 0.06, m["skin"], "character")
    parts["hand_r"] = sphere(f"{name}_hand_r", (0.31, -0.03, 0.7), 0.06, m["skin"], "character")
    if female:
        parts["skirt"] = cube(f"{name}_skirt", (0, 0, 0.67), (0.47, 0.28, 0.3), m["bottom"], "character", edge=0.05)
    parts["leg_l"] = cyl(f"{name}_leg_l", (-0.11, -0.02, 0.38), 0.055, 0.58, m["bottom"], "character", vertices=24)
    parts["leg_r"] = cyl(f"{name}_leg_r", (0.11, -0.02, 0.38), 0.055, 0.58, m["bottom"], "character", vertices=24)
    parts["shoe_l"] = cube(f"{name}_shoe_l", (-0.11, -0.08, 0.07), (0.16, 0.24, 0.07), m["shoe"], "character", edge=0.035)
    parts["shoe_r"] = cube(f"{name}_shoe_r", (0.11, -0.08, 0.07), (0.16, 0.24, 0.07), m["shoe"], "character", edge=0.035)
    return parts


def reset_pose(parts):
    for obj in parts.values():
        obj.rotation_euler = (0, 0, 0)


def pose(parts, mode, frame):
    reset_pose(parts)
    phase = math.sin(frame / 8 * math.tau)
    if mode == "walk":
        parts["arm_l"].rotation_euler[0] = phase * 0.45
        parts["arm_r"].rotation_euler[0] = -phase * 0.45
        parts["leg_l"].rotation_euler[0] = -phase * 0.35
        parts["leg_r"].rotation_euler[0] = phase * 0.35
        parts["shoe_l"].location.y = -0.08 + max(phase, 0) * 0.06
        parts["shoe_r"].location.y = -0.08 + max(-phase, 0) * 0.06
    else:
        for key in ("body", "head", "hair"):
            parts[key].location.z -= 0.22
        parts["arm_l"].rotation_euler[0] = 1.05 + phase * 0.04
        parts["arm_r"].rotation_euler[0] = 1.05 - phase * 0.04
        parts["hand_l"].location = (-0.24, -0.28, 0.64)
        parts["hand_r"].location = (0.24, -0.28, 0.64)
        parts["leg_l"].rotation_euler[0] = math.pi / 2
        parts["leg_r"].rotation_euler[0] = math.pi / 2
        parts["leg_l"].location = (-0.11, -0.22, 0.46)
        parts["leg_r"].location = (0.11, -0.22, 0.46)
        parts["shoe_l"].location = (-0.11, -0.47, 0.24)
        parts["shoe_r"].location = (0.11, -0.47, 0.24)
        if "skirt" in parts:
            parts["skirt"].location.z = 0.55
            parts["skirt"].rotation_euler[0] = 0.35


def render_character_set(kind, female):
    for obj in bpy.context.scene.objects:
        if obj.type not in {"CAMERA", "LIGHT"}:
            obj.hide_render = True
    bpy.ops.object.camera_add(location=(2.7, -4.0, 2.55))
    cam = bpy.context.object
    look_at(cam, (0, 0, 0.9))
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 2.15
    bpy.context.scene.camera = cam
    bpy.context.scene.render.resolution_x = 300
    bpy.context.scene.render.resolution_y = 360
    bpy.context.scene.render.film_transparent = True

    parts = make_character(kind, female)
    for obj in parts.values():
        obj.hide_render = False
    for anim in ("walk", "typing"):
        target = CHAR_DIR / kind / anim
        target.mkdir(parents=True, exist_ok=True)
        frames = 8 if anim == "walk" else 6
        for frame in range(frames):
            pose(parts, anim, frame)
            render(target / f"{frame:02d}.png")
    for obj in list(parts.values()) + [cam]:
        bpy.data.objects.remove(obj, do_unlink=True)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    CHAR_DIR.mkdir(parents=True)

    clear_scene()
    cam = setup_render()
    anchors = build_office()

    set_layers({"base"}, False)
    render(OUT / "office_base.png")
    set_layers({"shadow"}, True)
    render(OUT / "office_shadow.png")
    set_layers({"foreground"}, True)
    render(OUT / "office_foreground.png")
    set_layers({"glass"}, True)
    render(OUT / "office_glass.png")

    anchor_data = {
        "size": [WIDTH, HEIGHT],
        "anchors": {
            name: screen_anchor(cam, name, pos, 11.5 if name.startswith("walk") else 10.8, 20 + i)
            for i, (name, pos) in enumerate(anchors.items())
        },
        "walkPath": ["walk_a", "walk_b", "walk_c", "seat_main"],
        "people": [
            {"id": "lead", "kind": "female_01", "anchor": "walk_a", "mode": "walk", "z": 40, "interactive": True},
            {"id": "op_a", "kind": "male_01", "anchor": "seat_a", "mode": "typing", "z": 28},
            {"id": "op_b", "kind": "female_01", "anchor": "seat_b", "mode": "typing", "z": 29},
            {"id": "op_c", "kind": "male_01", "anchor": "seat_c", "mode": "typing", "z": 30},
            {"id": "producer", "kind": "female_01", "anchor": "seat_meet_a", "mode": "typing", "z": 35},
        ],
    }
    (OUT / "anchors.json").write_text(json.dumps(anchor_data, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "asset_source.json").write_text(
        json.dumps(
            {
                "source": "Blender offline render",
                "script": "scripts/render_25d_assets.py",
                "layers": ["office_base.png", "office_shadow.png", "office_foreground.png", "office_glass.png"],
                "status": "production pipeline v1, not final art replacement",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    (OUT / "collision.json").write_text(
        json.dumps(
            {
                "space": "world",
                "blocked": [
                    {"name": "left_wall", "points": [[-5.4, -3.35], [-5.15, -3.35], [-5.15, 3.35], [-5.4, 3.35]]},
                    {"name": "back_wall", "points": [[-5.4, 3.1], [5.4, 3.1], [5.4, 3.35], [-5.4, 3.35]]},
                    {"name": "desks", "points": [[-4.2, -2.4], [4.1, -2.4], [4.1, 2.35], [-4.2, 2.35]]},
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    render_character_set("female_01", True)
    render_character_set("male_01", False)
    print(f"wrote {OUT}")


main()
