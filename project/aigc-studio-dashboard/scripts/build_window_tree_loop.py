from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter


SIZE = (1536, 900)


WINDOW_POLYGON_SETS = {
    "v003": [
        [(0, 0), (585, 0), (520, 18), (320, 36), (0, 78)],
        [(1145, 0), (1536, 0), (1536, 48), (1410, 40), (1240, 24)],
    ],
    "v004": [
        [(0, 0), (520, 0), (515, 82), (410, 95), (170, 118), (0, 138)],
        [(1110, 0), (1536, 0), (1536, 138), (1360, 112), (1210, 86), (1110, 74)],
    ],
}


def cover_resize(image: Image.Image, size: tuple[int, int], scale: float = 1.0) -> Image.Image:
    tw, th = size
    sw, sh = image.size
    factor = max(tw / sw, th / sh) * scale
    resized = image.resize((round(sw * factor), round(sh * factor)), Image.Resampling.LANCZOS)
    left = (resized.width - tw) // 2
    top = (resized.height - th) // 2
    return resized.crop((left, top, left + tw, top + th))


def rolled(image: Image.Image, dx: int, dy: int) -> Image.Image:
    out = Image.new("RGBA", image.size)
    width, height = image.size
    for x in (-width, 0, width):
        for y in (-height, 0, height):
            out.alpha_composite(image, (dx + x, dy + y))
    return out.crop((0, 0, width, height))


def wave(image: Image.Image, phase: float, amplitude: float, band_height: int = 8) -> Image.Image:
    out = Image.new("RGBA", image.size)
    width, height = image.size
    for y in range(0, height, band_height):
        dy = min(band_height, height - y)
        shift = round(math.sin(phase + y * 0.025) * amplitude)
        strip = image.crop((0, y, width, y + dy))
        out.alpha_composite(rolled(strip, shift, 0), (0, y))
    return out


def build_mask(out_path: Path, polygons: list[list[tuple[int, int]]]) -> Image.Image:
    mask = Image.new("L", SIZE, 0)
    draw = ImageDraw.Draw(mask)
    for poly in polygons:
        draw.polygon(poly, fill=255)

    mask = mask.filter(ImageFilter.GaussianBlur(0.8))
    mask.save(out_path, optimize=True)
    return mask


def build_base_and_foreground(scene_base: Path, mask: Image.Image, interior_out: Path, foreground_out: Path) -> None:
    base = Image.open(scene_base).convert("RGBA")
    blur = base.filter(ImageFilter.GaussianBlur(22))
    tint = Image.new("RGBA", SIZE, (232, 222, 180, 255))
    clean = Image.blend(blur, tint, 0.34)
    interior = base.copy()
    interior.paste(clean, mask=mask)
    interior.save(interior_out, optimize=True)

    edge = ImageChops.difference(mask.filter(ImageFilter.MaxFilter(21)), mask.filter(ImageFilter.MinFilter(21)))
    edge = edge.point(lambda value: min(230, value * 2))
    foreground = base.copy()
    foreground.putalpha(edge)
    foreground.save(foreground_out, optimize=True)


def build_frames(source: Path, out_dir: Path, mask: Image.Image, count: int, alpha: int, motion_scale: float, tree_blur: float) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Image.open(source).convert("RGB")
    tree = ImageEnhance.Brightness(cover_resize(src, SIZE, 1.16)).enhance(0.86)
    tree = ImageEnhance.Contrast(tree).enhance(0.96)
    tree = ImageEnhance.Color(tree).enhance(0.9).convert("RGBA").filter(ImageFilter.GaussianBlur(tree_blur))
    frame_mask = mask.point(lambda value: round(value * max(0, min(alpha, 255)) / 255))

    for index in range(count):
        t = (math.tau * index) / count
        dx = round(math.sin(t) * 12 * motion_scale)
        dy = round(math.cos(t * 0.8) * 3 * motion_scale)
        frame = wave(rolled(tree, dx, dy), t, 4.5 * motion_scale)
        frame.putalpha(frame_mask)
        frame.save(out_dir / f"{index:02d}.png", optimize=True)


def build_contact_sheet(frames_dir: Path, out_path: Path) -> None:
    thumbs = []
    for index in range(0, 48, 6):
        frame = Image.open(frames_dir / f"{index:02d}.png").convert("RGBA")
        bg = Image.new("RGB", SIZE, (25, 32, 29))
        bg.paste(frame, mask=frame.getchannel("A"))
        thumbs.append(bg.resize((384, 225), Image.Resampling.LANCZOS))
    sheet = Image.new("RGB", (384 * 4, 225 * 2), (15, 18, 17))
    for index, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((index % 4) * 384, (index // 4) * 225))
    sheet.save(out_path, optimize=True)


def build_preview(interior_path: Path, frame_path: Path, foreground_path: Path, out_path: Path) -> None:
    interior = Image.open(interior_path).convert("RGBA")
    frame = Image.open(frame_path).convert("RGBA")
    foreground = Image.open(foreground_path).convert("RGBA")
    Image.alpha_composite(Image.alpha_composite(interior, frame), foreground).save(out_path, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--mask", required=True, type=Path)
    parser.add_argument("--frames", type=int, default=48)
    parser.add_argument("--contact-sheet", required=True, type=Path)
    parser.add_argument("--scene-base", type=Path)
    parser.add_argument("--interior-out", type=Path)
    parser.add_argument("--foreground-out", type=Path)
    parser.add_argument("--preview-out", type=Path)
    parser.add_argument("--polygon-set", choices=sorted(WINDOW_POLYGON_SETS), default="v003")
    parser.add_argument("--tree-alpha", type=int, default=255)
    parser.add_argument("--motion-scale", type=float, default=1.0)
    parser.add_argument("--tree-blur", type=float, default=0.8)
    args = parser.parse_args()

    mask = build_mask(args.mask, WINDOW_POLYGON_SETS[args.polygon_set])
    if args.scene_base and args.interior_out and args.foreground_out:
        build_base_and_foreground(args.scene_base, mask, args.interior_out, args.foreground_out)
    build_frames(args.source, args.out_dir, mask, args.frames, args.tree_alpha, args.motion_scale, args.tree_blur)
    build_contact_sheet(args.out_dir, args.contact_sheet)
    if args.interior_out and args.foreground_out and args.preview_out:
        build_preview(args.interior_out, args.out_dir / "00.png", args.foreground_out, args.preview_out)


if __name__ == "__main__":
    main()
