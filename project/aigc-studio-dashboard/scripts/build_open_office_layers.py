from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw


def polygon_points(poly):
    return [tuple(point) for point in poly]


def build_layers(scene_path: Path, base_path: Path, out_dir: Path, version: str) -> None:
    scene = json.loads(scene_path.read_text(encoding="utf-8"))
    width, height = scene["size"]
    out_dir.mkdir(parents=True, exist_ok=True)

    mask = Image.new("L", (width, height), 0)
    mask_draw = ImageDraw.Draw(mask)
    for poly in scene.get("walkablePolygons", []):
        mask_draw.polygon(polygon_points(poly), fill=255)
    for poly in scene.get("collisionZones", {}).values():
        mask_draw.polygon(polygon_points(poly), fill=0)
    mask.save(out_dir / f"open_office_walkable_mask_{version}.png", optimize=True)

    depth = Image.new("L", (width, height), 0)
    pixels = depth.load()
    for y in range(height):
        value = int(35 + 220 * (y / max(1, height - 1)))
        for x in range(width):
            pixels[x, y] = value
    depth.save(out_dir / f"open_office_depth_map_{version}.png", optimize=True)

    foreground = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    foreground.save(out_dir / f"open_office_foreground_occlusion_{version}.png", optimize=True)

    base = Image.open(base_path).convert("RGBA")
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for poly in scene.get("walkablePolygons", []):
        draw.polygon(polygon_points(poly), fill=(70, 220, 110, 58), outline=(70, 220, 110, 180))
    for poly in scene.get("collisionZones", {}).values():
        draw.polygon(polygon_points(poly), fill=(235, 70, 50, 52), outline=(235, 70, 50, 170))

    nodes = scene["navigation"]["nodes"]
    for start, end in scene["navigation"].get("edges", []):
        a = nodes[start]
        b = nodes[end]
        draw.line((a["x"], a["y"], b["x"], b["y"]), fill=(240, 200, 75, 230), width=5)

    patrol_colors = {
        "qc_left_loop": (40, 210, 255, 240),
        "qc_right_loop": (190, 110, 255, 240),
    }
    for route_name, route in scene["navigation"].get("patrolRoutes", {}).items():
        color = patrol_colors.get(route_name, (255, 255, 255, 220))
        for start, end in zip(route, route[1:]):
            a = nodes[start]
            b = nodes[end]
            draw.line((a["x"], a["y"], b["x"], b["y"]), fill=color, width=3)

    for name, point in nodes.items():
        x, y = point["x"], point["y"]
        outline = (255, 210, 70, 255)
        if name.startswith("qc_left"):
            outline = (40, 210, 255, 255)
        elif name.startswith("qc_right"):
            outline = (190, 110, 255, 255)
        draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=(16, 22, 30, 230), outline=outline, width=3)

    for group in scene.get("anchors", {}).values():
        for point in group.values():
            x, y = point["x"], point["y"]
            draw.rectangle((x - 8, y - 8, x + 8, y + 8), fill=(255, 215, 55, 245), outline=(20, 20, 20, 220))

    for point in scene.get("seatAnchors", {}).values():
        x, y = point["x"], point["y"]
        color = (110, 180, 255, 240) if point.get("genderSlot") == "male" else (255, 130, 190, 240)
        draw.rectangle((x - 6, y - 6, x + 6, y + 6), fill=color, outline=(255, 255, 255, 220))

    debug = Image.alpha_composite(base, overlay).convert("RGB")
    debug.save(out_dir / f"open_office_nav_debug_{version}.png", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", required=True, type=Path)
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    build_layers(args.scene, args.base, args.out_dir, args.version)


if __name__ == "__main__":
    main()
