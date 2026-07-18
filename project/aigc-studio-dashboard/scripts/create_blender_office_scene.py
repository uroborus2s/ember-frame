from __future__ import annotations

import math
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "public" / "assets" / "production-art" / "blender"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def mat(name, color, roughness=0.55, metallic=0.0, alpha=1.0, emission=None, emission_strength=0.0):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Alpha"].default_value = alpha
        if emission:
            bsdf.inputs["Emission Color"].default_value = emission
            bsdf.inputs["Emission Strength"].default_value = emission_strength
    material.diffuse_color = color
    if alpha < 1:
        material.blend_method = "BLEND"
        material.use_screen_refraction = True
        material.show_transparent_back = True
    return material


MATS = {}


def setup_materials():
    MATS.update(
        floor=mat("warm grey stone floor", (0.62, 0.61, 0.56, 1)),
        floor_line=mat("subtle floor grout", (0.46, 0.46, 0.42, 1)),
        wall=mat("warm white office wall", (0.82, 0.79, 0.7, 1)),
        wall_top=mat("white wall cap", (0.94, 0.91, 0.82, 1)),
        wood=mat("honey oak desks", (0.62, 0.39, 0.17, 1)),
        dark_wood=mat("dark walnut trim", (0.24, 0.15, 0.08, 1)),
        black=mat("soft black plastic", (0.015, 0.018, 0.02, 1), roughness=0.72),
        metal=mat("brushed dark metal", (0.28, 0.28, 0.27, 1), roughness=0.32, metallic=0.45),
        chair=mat("charcoal leather chairs", (0.06, 0.06, 0.055, 1), roughness=0.48),
        blue_screen=mat(
            "blue monitor glow",
            (0.025, 0.12, 0.2, 1),
            emission=(0.025, 0.36, 0.72, 1),
            emission_strength=1.15,
        ),
        cyan_screen=mat(
            "cyan screen highlight",
            (0.04, 0.45, 0.6, 1),
            emission=(0.02, 0.9, 1.0, 1),
            emission_strength=0.8,
        ),
        glass=mat("tempered blue glass", (0.58, 0.82, 0.92, 0.18), roughness=0.08, alpha=0.18),
        plant=mat("deep plant leaves", (0.08, 0.3, 0.13, 1)),
        plant2=mat("light plant leaves", (0.32, 0.48, 0.12, 1)),
        pot=mat("ceramic grey pot", (0.42, 0.38, 0.32, 1)),
        skin=mat("warm skin", (0.75, 0.48, 0.32, 1)),
        hair=mat("dark hair", (0.035, 0.025, 0.018, 1)),
        jacket_blue=mat("navy work jacket", (0.03, 0.08, 0.2, 1)),
        jacket_green=mat("teal work jacket", (0.04, 0.22, 0.2, 1)),
        jacket_brown=mat("brown work jacket", (0.22, 0.11, 0.06, 1)),
        paper=mat("warm paper", (0.88, 0.84, 0.72, 1)),
        server=mat("server black metal", (0.025, 0.03, 0.035, 1), roughness=0.42, metallic=0.2),
        server_light=mat(
            "server blue strips",
            (0.0, 0.25, 0.55, 1),
            emission=(0.0, 0.75, 1.0, 1),
            emission_strength=2.2,
        ),
        warm_light=mat(
            "warm led strip",
            (1.0, 0.62, 0.24, 1),
            emission=(1.0, 0.45, 0.12, 1),
            emission_strength=2.1,
        ),
    )


def cube(name, loc, scale, material, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material:
        obj.data.materials.append(material)
    if bevel:
        mod = obj.modifiers.new(f"{name} bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 3
        obj.modifiers.new(f"{name} weighted normals", "WEIGHTED_NORMAL")
    return obj


def cyl(name, loc, radius, depth, material, vertices=32, bevel=False):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    if material:
        obj.data.materials.append(material)
    if bevel:
        obj.modifiers.new(f"{name} weighted normals", "WEIGHTED_NORMAL")
    return obj


def sphere(name, loc, scale, material, segments=24):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=12, radius=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    if material:
        obj.data.materials.append(material)
    return obj


def rotate_z(obj, degrees):
    obj.rotation_euler[2] = math.radians(degrees)
    return obj


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def desk(name, x, y, w, d, rot=0):
    top = cube(f"{name} top", (x, y, 0.72), (w, d, 0.16), MATS["wood"], 0.04)
    rotate_z(top, rot)
    for sx in (-0.42, 0.42):
        for sy in (-0.38, 0.38):
            leg = cube(f"{name} leg", (x + sx * w, y + sy * d, 0.35), (0.08, 0.08, 0.7), MATS["dark_wood"], 0.015)
            rotate_z(leg, rot)
    return top


def monitor(name, x, y, rot=0, size=0.55):
    stand = cube(f"{name} stand", (x, y, 0.94), (0.08, 0.05, 0.34), MATS["black"], 0.01)
    screen = cube(f"{name} screen", (x, y, 1.18), (size, 0.04, size * 0.58), MATS["blue_screen"], 0.025)
    hi = cube(f"{name} screen line", (x, y - 0.023, 1.23), (size * 0.78, 0.012, 0.018), MATS["cyan_screen"], 0.004)
    for obj in (stand, screen, hi):
        rotate_z(obj, rot)
    return screen


def chair(name, x, y, rot=0):
    seat = cube(f"{name} seat", (x, y, 0.48), (0.5, 0.48, 0.12), MATS["chair"], 0.05)
    back = cube(f"{name} back", (x, y + 0.22, 0.84), (0.52, 0.1, 0.72), MATS["chair"], 0.05)
    stem = cyl(f"{name} stem", (x, y, 0.25), 0.05, 0.45, MATS["metal"], 16)
    for angle in (0, 72, 144, 216, 288):
        foot = cube(f"{name} wheel arm {angle}", (x, y, 0.08), (0.46, 0.035, 0.035), MATS["metal"], 0.01)
        rotate_z(foot, angle)
    for obj in (seat, back, stem):
        rotate_z(obj, rot)
    return seat


def person(name, x, y, rot=0, jacket="jacket_blue"):
    torso = cube(f"{name} torso", (x, y, 0.91), (0.34, 0.25, 0.52), MATS[jacket], 0.08)
    head = sphere(f"{name} head", (x, y - 0.03, 1.27), (0.14, 0.14, 0.16), MATS["skin"])
    hair = sphere(f"{name} hair", (x, y - 0.05, 1.36), (0.15, 0.13, 0.08), MATS["hair"])
    arm_l = cube(f"{name} left forearm", (x - 0.17, y - 0.18, 0.86), (0.08, 0.34, 0.07), MATS["skin"], 0.035)
    arm_r = cube(f"{name} right forearm", (x + 0.17, y - 0.18, 0.86), (0.08, 0.34, 0.07), MATS["skin"], 0.035)
    for obj in (torso, head, hair, arm_l, arm_r):
        rotate_z(obj, rot)
    return torso


def plant(name, x, y, scale=1.0):
    cyl(f"{name} pot", (x, y, 0.2), 0.18 * scale, 0.4 * scale, MATS["pot"], 24)
    for i in range(10):
        angle = i * 36
        leaf = sphere(
            f"{name} leaf {i}",
            (x + math.cos(math.radians(angle)) * 0.13 * scale, y + math.sin(math.radians(angle)) * 0.13 * scale, 0.54 + (i % 3) * 0.06 * scale),
            (0.08 * scale, 0.22 * scale, 0.035 * scale),
            MATS["plant" if i % 2 else "plant2"],
            16,
        )
        leaf.rotation_euler[2] = math.radians(angle)
        leaf.rotation_euler[0] = math.radians(24)


def shelf(name, x, y, w, rot=0):
    body = cube(f"{name} body", (x, y, 1.0), (w, 0.28, 1.8), MATS["dark_wood"], 0.03)
    rotate_z(body, rot)
    for z in (0.45, 0.82, 1.2, 1.55):
        board = cube(f"{name} shelf {z}", (x, y - 0.01, z), (w * 0.94, 0.31, 0.045), MATS["wood"], 0.01)
        rotate_z(board, rot)
    for i in range(8):
        bx = x - w * 0.38 + (i % 4) * w * 0.23
        bz = 0.58 + (i // 4) * 0.54
        book = cube(f"{name} book {i}", (bx, y - 0.16, bz), (0.08, 0.08, 0.26), MATS["paper"], 0.005)
        rotate_z(book, rot)


def server_rack(name, x, y, rot=0):
    rack = cube(f"{name} rack", (x, y, 1.0), (0.55, 0.48, 1.9), MATS["server"], 0.05)
    rotate_z(rack, rot)
    for z in (0.45, 0.7, 0.95, 1.2, 1.45):
        strip = cube(f"{name} light {z}", (x, y - 0.25, z), (0.36, 0.025, 0.035), MATS["server_light"], 0.004)
        rotate_z(strip, rot)


def wall(name, x, y, w, d, h=1.2):
    base = cube(name, (x, y, h / 2), (w, d, h), MATS["wall"], 0.015)
    cap = cube(f"{name} cap", (x, y, h + 0.05), (w + 0.02, d + 0.02, 0.1), MATS["wall_top"], 0.02)
    return base, cap


def glass_wall(name, x, y, w, rot=0):
    pane = cube(name, (x, y, 0.95), (w, 0.035, 1.7), MATS["glass"], 0.02)
    rail = cube(f"{name} rail", (x, y, 1.82), (w, 0.045, 0.04), MATS["metal"], 0.01)
    for obj in (pane, rail):
        rotate_z(obj, rot)


def add_floor_grid():
    cube("main floor slab", (0, 0, -0.035), (13.5, 9.0, 0.07), MATS["floor"], 0.03)
    cube("soft warm floor band", (-3.9, 2.7, -0.02), (3.2, 1.25, 0.012), MATS["paper"], 0.02)
    cube("soft warm floor band 2", (3.6, -2.7, -0.018), (3.8, 1.1, 0.012), MATS["paper"], 0.02)
    for x in [i * 0.75 - 6.75 for i in range(19)]:
        cube("floor vertical grout", (x, 0, 0.006), (0.012, 9.0, 0.006), MATS["floor_line"])
    for y in [i * 0.75 - 4.5 for i in range(13)]:
        cube("floor horizontal grout", (0, y, 0.008), (13.5, 0.012, 0.006), MATS["floor_line"])


def build_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    setup_materials()
    add_floor_grid()

    # Room walls and glass corridors.
    wall("top office left wall", -0.9, 2.95, 5.0, 0.16)
    wall("top office back wall", -0.9, 4.7, 5.0, 0.16)
    wall("left console back wall", -4.35, 0.75, 3.7, 0.16)
    wall("meeting back wall", -3.2, -2.75, 4.1, 0.16)
    wall("bottom console back wall", 3.1, -2.45, 4.2, 0.16)
    wall("recording booth wall", 5.25, 0.15, 0.16, 3.0)
    glass_wall("central glass wall", 1.65, 0.4, 3.9, 90)
    glass_wall("server room glass", 4.15, 2.2, 3.4, 0)

    # Upper working office.
    for row, y in enumerate((3.95, 3.12)):
        for col, x in enumerate((-1.95, -0.65, 0.65)):
            desk(f"top desk {row}-{col}", x, y, 1.05, 0.72)
            monitor(f"top monitor {row}-{col}", x, y - 0.18, 0, 0.5)
            chair(f"top chair {row}-{col}", x, y - 0.64, 180)
            person(f"top worker {row}-{col}", x, y - 0.52, 180, ["jacket_blue", "jacket_green", "jacket_brown"][(row + col) % 3])

    shelf("top book shelf left", -3.55, 3.95, 0.72)
    shelf("top book shelf back", 1.9, 4.55, 1.0)
    shelf("top book shelf back 2", 3.0, 4.55, 1.0)

    # Left curved console, approximated as segmented desks.
    for i, angle in enumerate((-32, -12, 12, 32)):
        x = -4.0 + i * 0.55
        y = 0.0 + abs(i - 1.5) * 0.08
        desk(f"left console segment {i}", x, y, 0.72, 0.5, angle)
        monitor(f"left console monitor {i}", x, y - 0.15, angle, 0.48)
    chair("left console chair", -3.2, -0.75, 180)
    person("left console worker", -3.2, -0.6, 180, "jacket_blue")

    # Meeting room.
    desk("meeting table", -3.1, -3.45, 3.1, 1.25)
    meeting_people = [(-4.0, -4.25, 0), (-3.2, -4.38, 0), (-2.35, -4.2, 0), (-4.0, -2.68, 180), (-3.15, -2.58, 180), (-2.25, -2.72, 180)]
    for i, (x, y, rot) in enumerate(meeting_people):
        chair(f"meeting chair {i}", x, y, rot)
        person(f"meeting worker {i}", x, y + (0.16 if rot == 0 else -0.16), rot, ["jacket_blue", "jacket_green", "jacket_brown"][i % 3])
    for i, x in enumerate((-3.9, -3.25, -2.55)):
        cube(f"meeting paper {i}", (x, -3.35, 0.83), (0.34, 0.22, 0.012), MATS["paper"], 0.005)

    # Bottom right console.
    for i, angle in enumerate((-25, 0, 25)):
        x = 2.45 + i * 0.58
        y = -2.75 + abs(i - 1) * 0.07
        desk(f"bottom console segment {i}", x, y, 0.82, 0.54, angle)
        monitor(f"bottom console monitor {i}", x, y - 0.16, angle, 0.55)
    chair("bottom console chair", 3.0, -3.55, 180)
    person("bottom console worker", 3.0, -3.38, 180, "jacket_blue")

    # Server and recording rooms.
    for i, x in enumerate((3.2, 4.05, 4.9)):
        server_rack(f"server rack {i}", x, 3.4, 0)
    cube("recording booth floor wood", (5.9, -1.45, 0.02), (2.1, 2.2, 0.04), MATS["wood"], 0.02)
    for i, x in enumerate((5.4, 6.2)):
        cyl(f"recording stool {i}", (x, -1.55, 0.48), 0.18, 0.08, MATS["chair"], 32)
        cyl(f"recording stool stem {i}", (x, -1.55, 0.25), 0.04, 0.45, MATS["metal"], 16)
    cyl("microphone stand 1", (5.6, -0.7, 0.75), 0.025, 1.15, MATS["black"], 12)
    cyl("microphone stand 2", (6.35, -0.6, 0.75), 0.025, 1.15, MATS["black"], 12)
    cube("recording warm led", (5.9, -0.38, 1.62), (1.85, 0.035, 0.05), MATS["warm_light"], 0.01)

    # Screens, plants, decor.
    cube("large review screen", (-5.2, 2.8, 1.35), (1.8, 0.05, 1.0), MATS["blue_screen"], 0.04)
    cube("wall video board", (-4.25, -1.25, 1.25), (2.0, 0.05, 0.9), MATS["blue_screen"], 0.035)
    for i, (x, y, s) in enumerate(((-5.85, 3.7, 1.0), (-5.75, -2.4, 0.9), (-1.95, 2.35, 0.8), (1.4, 1.35, 0.85), (4.3, 0.2, 0.9), (6.15, -0.1, 0.85), (2.2, -2.1, 0.75))):
        plant(f"plant {i}", x, y, s)

    # Small desk clutter.
    for i, (x, y) in enumerate(((-2.1, 3.7), (-0.6, 3.0), (0.7, 3.8), (-3.5, -3.5), (3.2, -2.9), (2.3, -2.7))):
        cube(f"paper stack {i}", (x, y, 0.83), (0.28, 0.18, 0.025), MATS["paper"], 0.004)
        cyl(f"desk cup {i}", (x + 0.23, y + 0.1, 0.9), 0.045, 0.12, MATS["pot"], 16)


def setup_camera_and_render():
    bpy.ops.object.light_add(type="SUN", location=(0, 0, 8))
    sun = bpy.context.object
    sun.name = "large soft sun"
    sun.data.energy = 1.45
    sun.rotation_euler = (math.radians(50), 0, math.radians(-35))

    bpy.ops.object.light_add(type="AREA", location=(-3.5, -4.0, 6.0))
    area = bpy.context.object
    area.name = "warm window fill"
    area.data.energy = 620
    area.data.size = 6.5

    bpy.ops.object.light_add(type="AREA", location=(3.8, 3.2, 4.2))
    cool = bpy.context.object
    cool.name = "cool server fill"
    cool.data.energy = 150
    cool.data.size = 4.0
    cool.data.color = (0.55, 0.78, 1.0)

    bpy.ops.object.camera_add(location=(8.8, -9.7, 8.6))
    camera = bpy.context.object
    look_at(camera, (0.0, -0.1, 0.42))
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 12.2
    bpy.context.scene.camera = camera

    scene = bpy.context.scene
    scene.render.resolution_x = 1536
    scene.render.resolution_y = 900
    scene.render.film_transparent = False
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 96
    scene.cycles.use_denoising = True
    scene.world.color = (0.03, 0.035, 0.038)
    scene.view_settings.view_transform = "Filmic"
    scene.view_settings.look = "Medium High Contrast"
    scene.view_settings.exposure = 0.12
    scene.view_settings.gamma = 1


def main():
    build_scene()
    setup_camera_and_render()
    blend_path = OUT_DIR / "aigc_studio_office_source.blend"
    render_path = OUT_DIR / "aigc_studio_office_blender_preview_v2.png"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    bpy.context.scene.render.filepath = str(render_path)
    bpy.ops.render.render(write_still=True)
    print(f"BLEND={blend_path}")
    print(f"RENDER={render_path}")


if __name__ == "__main__":
    main()
