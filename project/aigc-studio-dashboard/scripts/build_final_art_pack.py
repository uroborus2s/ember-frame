from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "public" / "assets" / "final-art"
OUT = ROOT / "public" / "assets" / "production-art"
SCENE = OUT / "scene"
CHARACTERS = OUT / "characters"

SCENE_SIZE = (1536, 900)
FRAME_SIZE = (300, 360)
DIRECTIONS = ("NE", "NW", "SE", "SW")
OCCLUDER_SPECS = {
    "left_console_lip": {"box": (142, 370, 502, 525), "z": 42},
    "left_console_desk_edge": {
        "z": 43,
        "polygons": [[(146, 390), (500, 366), (524, 412), (410, 464), (176, 470)]],
    },
    "left_chair_back": {
        "z": 44,
        "polygons": [[(330, 455), (448, 450), (456, 514), (428, 542), (328, 526), (318, 488)]],
    },
    "left_chair_seat_front": {
        "z": 45,
        "polygons": [[(324, 486), (448, 486), (452, 526), (410, 546), (326, 524)]],
    },
    "meeting_table_front": {"box": (260, 654, 690, 875), "z": 45},
    "control_console_lip": {
        "z": 47,
        "polygons": [
            [(838, 626), (958, 616), (964, 644), (842, 670)],
            [(1110, 632), (1268, 646), (1260, 704), (1140, 698)],
        ],
    },
    "desk_edge_mask": {
        "z": 48,
        "polygons": [
            [(842, 666), (940, 686), (918, 708), (836, 682)],
            [(1090, 668), (1238, 704), (1120, 712), (1048, 686)],
        ],
    },
    "chair_back_control": {
        "z": 49,
        "polygons": [
            [(910, 690), (956, 682), (966, 752), (938, 758), (906, 718)],
            [(1058, 682), (1100, 698), (1084, 746), (1048, 752)],
        ],
    },
    "chair_seat_front_mask": {
        "z": 50,
        "polygons": [[(920, 706), (1098, 704), (1118, 738), (1080, 766), (952, 766), (908, 736)]],
    },
    "recording_booth_front": {"box": (1180, 642, 1528, 882), "z": 55},
    "glass_wall_mid": {"box": (555, 470, 715, 632), "z": 50},
}


def clean_key(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a and r > 145 and b > 125 and g < 90:
                pixels[x, y] = (r, g, b, 0)
    return image


def remove_green_key(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if a and g > 145 and g > r * 1.35 and g > b * 1.35:
                pixels[x, y] = (r, g, b, 0)
    return image


def alpha_bbox(image: Image.Image, threshold: int = 32):
    alpha = image.getchannel("A")
    mask = alpha.point(lambda value: 255 if value > threshold else 0)
    return mask.getbbox()


def crop_subject(image: Image.Image) -> Image.Image:
    bbox = alpha_bbox(image)
    return image.crop(bbox) if bbox else image


def sheet_frames(path: Path, expected_count: int) -> list[Image.Image]:
    source = clean_key(Image.open(path))
    alpha = source.getchannel("A")
    active_columns = []
    for x in range(source.width):
        active_columns.append(alpha.crop((x, 0, x + 1, source.height)).getextrema()[1] > 80)

    runs = []
    start = None
    for index, active in enumerate(active_columns + [False]):
        if active and start is None:
            start = index
        if not active and start is not None:
            if index - start > 12:
                runs.append((start, index))
            start = None

    if len(runs) != expected_count:
        width = source.width // expected_count
        runs = [(index * width, (index + 1) * width) for index in range(expected_count)]

    frames = []
    for left, right in runs[:expected_count]:
        frame = crop_subject(source.crop((max(left - 4, 0), 0, min(right + 4, source.width), source.height)))
        frames.append(frame)
    return frames


def transition_sheet_frames(path: Path, expected_count: int = 8) -> list[Image.Image]:
    source = remove_green_key(Image.open(path))
    alpha = source.getchannel("A")
    runs = []
    start = None
    for index in range(source.width + 1):
        active = False
        if index < source.width:
            active = alpha.crop((index, 0, index + 1, source.height)).getextrema()[1] > 12
        if active and start is None:
            start = index
        if not active and start is not None:
            if index - start > 30:
                runs.append((start, index))
            start = None

    if len(runs) != expected_count:
        width = source.width // expected_count
        runs = [(index * width, (index + 1) * width) for index in range(expected_count)]

    cropped = []
    for left, right in runs[:expected_count]:
        frame = source.crop((max(left - 8, 0), 0, min(right + 8, source.width), source.height))
        cropped.append(crop_subject(frame))
    frames = normalize_frames_consistent(cropped)
    if len(frames) != expected_count:
        raise RuntimeError(f"{path} yielded {len(frames)} transition frames")
    return frames


def transition_frames_for(name: str, action: str, direction: str) -> list[Image.Image]:
    path = SRC / f"{name}-{action}-{direction}-sheet.png"
    if not path.exists():
        raise RuntimeError(f"missing redrawn transition sheet: {path}")
    return transition_sheet_frames(path)


def control_frames_for(name: str, action: str) -> list[Image.Image]:
    path = SRC / f"{name}-{action}-control-sheet.png"
    if not path.exists():
        raise RuntimeError(f"missing control seat transition sheet: {path}")
    return transition_sheet_frames(path, 6 if action == "typing" else 8)


def normalize_frame(image: Image.Image, max_height: int = 330, max_width: int = 236) -> Image.Image:
    subject = crop_subject(image)
    if subject.width == 0 or subject.height == 0:
        return Image.new("RGBA", FRAME_SIZE, (0, 0, 0, 0))

    scale = min(max_width / subject.width, max_height / subject.height)
    size = (max(1, round(subject.width * scale)), max(1, round(subject.height * scale)))
    subject = subject.resize(size, Image.Resampling.LANCZOS)

    frame = Image.new("RGBA", FRAME_SIZE, (0, 0, 0, 0))
    x = (FRAME_SIZE[0] - subject.width) // 2
    y = FRAME_SIZE[1] - subject.height - 18
    frame.alpha_composite(subject, (x, y))
    return frame


def normalize_frames_consistent(images: list[Image.Image], max_height: int = 330, max_width: int = 236) -> list[Image.Image]:
    subjects = [crop_subject(image) for image in images]
    width = max((subject.width for subject in subjects), default=1)
    height = max((subject.height for subject in subjects), default=1)
    scale = min(max_width / width, max_height / height)
    frames = []
    for subject in subjects:
        if subject.width == 0 or subject.height == 0:
            frames.append(Image.new("RGBA", FRAME_SIZE, (0, 0, 0, 0)))
            continue
        size = (max(1, round(subject.width * scale)), max(1, round(subject.height * scale)))
        subject = subject.resize(size, Image.Resampling.LANCZOS)
        frame = Image.new("RGBA", FRAME_SIZE, (0, 0, 0, 0))
        x = (FRAME_SIZE[0] - subject.width) // 2
        y = FRAME_SIZE[1] - subject.height - 18
        frame.alpha_composite(subject, (x, y))
        frames.append(frame)
    return frames


def scene_grade(frame: Image.Image) -> Image.Image:
    frame = frame.convert("RGBA")
    alpha = frame.getchannel("A")
    rgb = frame.convert("RGB")
    rgb = ImageEnhance.Color(rgb).enhance(0.72)
    rgb = ImageEnhance.Contrast(rgb).enhance(0.9)
    rgb = ImageEnhance.Brightness(rgb).enhance(0.86)
    r, g, b = rgb.split()
    r = r.point(lambda value: min(255, round(value * 1.04)))
    g = g.point(lambda value: round(value * 0.98))
    b = b.point(lambda value: round(value * 0.88))
    result = Image.merge("RGBA", (r, g, b, alpha))
    pixels = result.load()
    for y in range(result.height):
        for x in range(result.width):
            red, green, blue, opacity = pixels[x, y]
            if 0 < opacity < 230 and green > red * 1.05 and green > blue * 1.05:
                pixels[x, y] = (red, round((red + blue) * 0.5), blue, opacity)
    return result


def flip_if_west(frame: Image.Image, direction: str) -> Image.Image:
    return ImageOps.mirror(frame) if direction.endswith("W") else frame.copy()


def save_sequence(frames: list[Image.Image], directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for index, frame in enumerate(frames):
        scene_grade(frame).save(directory / f"{index:02d}.png")


def breathing_frames(frame: Image.Image) -> list[Image.Image]:
    frames = []
    for offset in (0, -1, 0, 1):
        canvas = Image.new("RGBA", FRAME_SIZE, (0, 0, 0, 0))
        canvas.alpha_composite(frame, (0, offset))
        frames.append(canvas)
    return frames


def transition_origins(start_y: int, end_y: int, count: int) -> list[list[int]]:
    return [[150, round(start_y + (end_y - start_y) * index / (count - 1))] for index in range(count)]


def make_master_cards(character_dir: Path, walk: list[Image.Image], typing: list[Image.Image]) -> None:
    master = character_dir / "master"
    master.mkdir(parents=True, exist_ok=True)

    threeview = Image.new("RGBA", (900, 360), (0, 0, 0, 0))
    views = [walk[1], walk[3], ImageEnhance.Brightness(ImageOps.mirror(walk[1])).enhance(0.82)]
    for index, view in enumerate(views):
        threeview.alpha_composite(view, (index * 300, 0))
    threeview.save(master / "threeview.png")

    detail = Image.new("RGBA", (900, 360), (0, 0, 0, 0))
    crops = [
        walk[0].crop((92, 36, 208, 150)),
        walk[0].crop((86, 128, 214, 242)),
        typing[1].crop((72, 120, 228, 245)),
    ]
    for index, crop in enumerate(crops):
        crop = crop.resize((220, 220), Image.Resampling.LANCZOS)
        detail.alpha_composite(crop, (50 + index * 300, 70))
    detail.save(master / "detail_crops.png")


def build_character(name: str) -> None:
    character_id = f"{name}_01"
    character_dir = CHARACTERS / character_id
    raw_walk = [normalize_frame(frame) for frame in sheet_frames(SRC / f"{name}-walksheet-alpha.png", 8)]
    raw_typing = [normalize_frame(frame, max_height=308, max_width=230) for frame in sheet_frames(SRC / f"{name}-typing-sheet-alpha.png", 6)]
    make_master_cards(character_dir, raw_walk, raw_typing)

    frame_counts = {"idle": 4, "walk": 8, "sit": 8, "seated": 4, "typing": 6, "stand": 8}
    anchors = {}
    for direction in DIRECTIONS:
        walk = [flip_if_west(frame, direction) for frame in raw_walk]
        typing = [flip_if_west(frame, direction) for frame in raw_typing]
        sit = transition_frames_for(name, "sit", direction)
        stand = transition_frames_for(name, "stand", direction)
        groups = {
            f"idle_{direction}": breathing_frames(walk[0]),
            f"walk_{direction}": walk,
            f"sit_{direction}": sit,
            f"seated_{direction}": typing[:4],
            f"typing_{direction}": typing,
            f"stand_{direction}": stand,
        }
        for group, frames in groups.items():
            save_sequence(frames, character_dir / "sprites" / group)
            action = group.split("_", 1)[0]
            per_frame_origins = None
            if action == "sit":
                per_frame_origins = transition_origins(330, 300, frame_counts[action])
            elif action == "stand":
                per_frame_origins = transition_origins(300, 330, frame_counts[action])

            anchor = {
                "origin": per_frame_origins[0] if per_frame_origins else [150, 330 if action in {"idle", "walk"} else 300],
                "anchorType": "feet" if action in {"idle", "walk"} else "feet_to_hips" if action == "sit" else "hips_to_feet" if action == "stand" else "hips",
                "frameCount": frame_counts[action],
            }
            if per_frame_origins:
                anchor["perFrameOrigins"] = per_frame_origins
            anchors[group] = anchor

    if name == "female":
        control_groups = {
            "sit_control": control_frames_for(name, "sit"),
            "typing_control": control_frames_for(name, "typing"),
            "stand_control": control_frames_for(name, "stand"),
        }
        for group, frames in control_groups.items():
            save_sequence(frames, character_dir / "sprites" / group)
            action = group.split("_", 1)[0]
            per_frame_origins = None
            if action == "sit":
                per_frame_origins = transition_origins(330, 300, len(frames))
            elif action == "stand":
                per_frame_origins = transition_origins(300, 330, len(frames))
            anchor = {
                "origin": per_frame_origins[0] if per_frame_origins else [150, 300],
                "anchorType": "feet_to_hips" if action == "sit" else "hips_to_feet" if action == "stand" else "hips",
                "frameCount": len(frames),
            }
            if per_frame_origins:
                anchor["perFrameOrigins"] = per_frame_origins
            anchors[group] = anchor

    meta = {
        "characterId": character_id,
        "frameSize": list(FRAME_SIZE),
        "directions": list(DIRECTIONS),
        "actions": frame_counts,
        "anchors": anchors,
        "assetStatus": {
            "sit": "redrawn_independent_four_direction_transition_sheets",
            "stand": "redrawn_independent_four_direction_transition_sheets",
        },
        "sourceSheets": {
            "walk": f"public/assets/final-art/{name}-walksheet-alpha.png",
            "typing": f"public/assets/final-art/{name}-typing-sheet-alpha.png",
            **{
                f"{action}_{direction}": f"public/assets/final-art/{name}-{action}-{direction}-sheet.png"
                for action in ("sit", "stand")
                for direction in DIRECTIONS
            },
            **(
                {
                    "sit_control": "public/assets/final-art/female-sit-control-sheet.png",
                    "typing_control": "public/assets/final-art/female-typing-control-sheet.png",
                    "stand_control": "public/assets/final-art/female-stand-control-sheet.png",
                }
                if name == "female"
                else {}
            ),
        },
    }
    (character_dir / "sprite_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def fit_scene(image: Image.Image) -> Image.Image:
    scale = SCENE_SIZE[1] / image.height
    resized = image.resize((round(image.width * scale), SCENE_SIZE[1]), Image.Resampling.LANCZOS)
    left = (resized.width - SCENE_SIZE[0]) // 2
    return resized.crop((left, 0, left + SCENE_SIZE[0], SCENE_SIZE[1]))


def draw_soft_ellipse(layer: Image.Image, box, color, blur: int = 12) -> None:
    patch = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(patch)
    draw.ellipse(box, fill=color)
    layer.alpha_composite(patch.filter(ImageFilter.GaussianBlur(blur)))


def build_foreground(base: Image.Image) -> Image.Image:
    foreground = Image.new("RGBA", SCENE_SIZE, (0, 0, 0, 0))
    for spec in OCCLUDER_SPECS.values():
        foreground.alpha_composite(render_occluder(base, spec))
    return foreground


def render_occluder(base: Image.Image, spec: dict) -> Image.Image:
    layer = Image.new("RGBA", SCENE_SIZE, (0, 0, 0, 0))
    if "polygons" in spec:
        mask = Image.new("L", SCENE_SIZE, 0)
        draw = ImageDraw.Draw(mask)
        for polygon in spec["polygons"]:
            draw.polygon(polygon, fill=255)
        source = base.copy().convert("RGBA")
        source.putalpha(mask.filter(ImageFilter.GaussianBlur(0.4)))
        layer.alpha_composite(source)
        return layer

    box = spec["box"]
    layer.alpha_composite(base.crop(box).convert("RGBA"), box[:2])
    return layer


def build_occluders(base: Image.Image) -> None:
    occluders = SCENE / "occluders"
    occluders.mkdir(parents=True, exist_ok=True)
    for name, spec in OCCLUDER_SPECS.items():
        render_occluder(base, spec).save(occluders / f"{name}.png")


def build_glass() -> Image.Image:
    glass = Image.new("RGBA", SCENE_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(glass, "RGBA")
    for polygon in (
        [(520, 220), (735, 290), (716, 565), (505, 486)],
        [(850, 178), (1184, 168), (1234, 455), (902, 500)],
        [(710, 530), (820, 586), (818, 862), (704, 802)],
    ):
        draw.polygon(polygon, fill=(160, 218, 230, 38), outline=(226, 252, 255, 72))
    for line in ((520, 220, 716, 565), (625, 252, 606, 524), (1000, 175, 1060, 478), (1134, 170, 1190, 468)):
        draw.line(line, fill=(238, 255, 255, 95), width=3)
    return glass.filter(ImageFilter.GaussianBlur(0.35))


def build_shadow() -> Image.Image:
    shadow = Image.new("RGBA", SCENE_SIZE, (0, 0, 0, 0))
    for box in (
        (824, 512, 1046, 598),
        (914, 650, 1252, 784),
        (270, 454, 506, 552),
        (320, 742, 650, 860),
        (700, 506, 822, 588),
    ):
        draw_soft_ellipse(shadow, box, (0, 0, 0, 42), 14)
    return shadow


def build_walkable_mask() -> Image.Image:
    mask = Image.new("L", SCENE_SIZE, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon([(318, 506), (554, 500), (566, 536), (508, 562), (334, 556), (304, 526)], fill=255)
    return Image.merge("RGB", (mask, mask, mask))


def build_depth_map() -> Image.Image:
    depth = Image.new("L", SCENE_SIZE)
    pixels = depth.load()
    for y in range(SCENE_SIZE[1]):
        value = int(45 + (y / (SCENE_SIZE[1] - 1)) * 190)
        for x in range(SCENE_SIZE[0]):
            pixels[x, y] = value
    return Image.merge("RGB", (depth, depth, depth))


def build_top_view_control() -> Image.Image:
    image = Image.new("RGB", SCENE_SIZE, "#eef3f1")
    draw = ImageDraw.Draw(image)
    draw.rectangle((80, 80, 1456, 820), outline="#24373a", width=6)
    zones = [
        ("screen lounge", (105, 95, 462, 305), "#d8eadb"),
        ("left console", (120, 350, 535, 545), "#f2d8a7"),
        ("open hall", (570, 340, 1030, 690), "#ffffff"),
        ("server room", (1038, 100, 1432, 330), "#d5e4f5"),
        ("recording booth", (1130, 420, 1430, 675), "#f5dfbd"),
        ("meeting table", (250, 635, 690, 795), "#f2d8a7"),
        ("control console", (820, 635, 1280, 810), "#f2d8a7"),
    ]
    for label, box, color in zones:
        draw.rectangle(box, fill=color, outline="#445b5e", width=3)
        draw.text((box[0] + 10, box[1] + 10), label, fill="#15282b")

    path = [(520, 522), (475, 524), (435, 526), (398, 528), (405, 500)]
    draw.line(path, fill="#2b77c0", width=8, joint="curve")
    for index, point in enumerate(path, 1):
        x, y = point
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill="#2b77c0")
        draw.text((x + 16, y - 14), f"walk_{index}", fill="#102c55")

    seats = [
        (1008, 705, "seat_control", -72, 34),
        (375, 492, "seat_left", 22, -12),
        (380, 735, "seat_meet_a", 22, -12),
        (550, 735, "seat_meet_b", 22, -12),
    ]
    for x, y, label, dx, dy in seats:
        draw.rectangle((x - 18, y - 18, x + 18, y + 18), fill="#dc5b45")
        draw.text((x + dx, y + dy), label, fill="#6e2118")

    draw.text((95, 835), "CONTROL ONLY: walkable zones, blocked furniture, seat anchors, foreground occluders", fill="#15282b")
    return image


def scene_manifest() -> dict:
    anchors = {
        "walk_a": {"name": "walk_a", "x": 520, "y": 522, "widthPct": 4.8, "z": 41},
        "walk_b": {"name": "walk_b", "x": 475, "y": 524, "widthPct": 4.8, "z": 41},
        "walk_c": {"name": "walk_c", "x": 435, "y": 526, "widthPct": 4.8, "z": 41},
        "walk_d": {"name": "walk_d", "x": 398, "y": 528, "widthPct": 4.8, "z": 41},
        "seat_control": {"name": "seat_control", "x": 1008, "y": 705, "widthPct": 5.5, "z": 46},
        "seat_left_console": {"name": "seat_left_console", "x": 405, "y": 500, "widthPct": 4.8, "z": 40},
        "seat_meeting_a": {"name": "seat_meeting_a", "x": 380, "y": 735, "widthPct": 4.7, "z": 42},
        "seat_meeting_b": {"name": "seat_meeting_b", "x": 550, "y": 735, "widthPct": 4.5, "z": 43},
        "staff_a": {"name": "staff_a", "x": 695, "y": 540, "widthPct": 4.3, "z": 35},
        "producer": {"name": "producer", "x": 610, "y": 648, "widthPct": 4.5, "z": 36},
    }
    return {
        "size": list(SCENE_SIZE),
        "layers": {
            "base": "scene/office_base.png",
            "shadow": "scene/office_shadow.png",
            "foreground": "scene/office_foreground.png",
            "glass": "scene/office_glass.png",
            "walkableMask": "scene/walkable_mask.png",
            "depthMap": "scene/depth_map.png",
            "topViewControl": "scene/top_view_control.png",
        },
        "occluders": {
            name: {"src": f"scene/occluders/{name}.png", "z": spec["z"]}
            for name, spec in OCCLUDER_SPECS.items()
        },
        "sceneOccluders": ["glass_wall_mid", "recording_booth_front"],
        "walkNodes": {key: {"x": value["x"], "y": value["y"]} for key, value in anchors.items() if key.startswith("walk_")},
        "walkEdges": [["walk_a", "walk_b"], ["walk_b", "walk_c"], ["walk_c", "walk_d"], ["walk_d", "seat_left_console"]],
        "seats": [
            {
                "id": "seat_control",
                "label": "control console seat",
                "approach": {"x": anchors["walk_c"]["x"], "y": anchors["walk_c"]["y"]},
                "sit": {"x": anchors["seat_control"]["x"], "y": anchors["seat_control"]["y"]},
                "facing": "NE",
                "z": 46,
                "occluders": ["control_console_lip", "desk_edge_mask", "chair_back_control", "chair_seat_front_mask"],
                "animations": {"sit": "sit_NE", "seated": "typing_NE", "stand": "stand_NE"},
            },
            {
                "id": "seat_left_console",
                "label": "left console seat",
                "approach": {"x": anchors["walk_d"]["x"], "y": anchors["walk_d"]["y"]},
                "stand": {"x": anchors["walk_d"]["x"], "y": anchors["walk_d"]["y"], "widthPct": anchors["walk_d"]["widthPct"], "z": anchors["walk_d"]["z"]},
                "sit": {"x": anchors["seat_left_console"]["x"], "y": anchors["seat_left_console"]["y"]},
                "facing": "NE",
                "z": 40,
                "occluders": ["left_chair_back"],
                "transitionOccluders": ["left_chair_seat_front"],
                "animations": {"sit": "sit_control", "seated": "typing_control", "stand": "stand_control"},
            },
            {
                "id": "seat_meeting_a",
                "label": "meeting seat A",
                "approach": {"x": 430, "y": 690},
                "sit": {"x": anchors["seat_meeting_a"]["x"], "y": anchors["seat_meeting_a"]["y"]},
                "facing": "NE",
                "z": 42,
                "occluders": ["meeting_table_front"],
                "animations": {"sit": "sit_NE", "seated": "typing_NE", "stand": "stand_NE"},
            },
            {
                "id": "seat_meeting_b",
                "label": "meeting seat B",
                "approach": {"x": 580, "y": 690},
                "sit": {"x": anchors["seat_meeting_b"]["x"], "y": anchors["seat_meeting_b"]["y"]},
                "facing": "NW",
                "z": 43,
                "occluders": ["meeting_table_front"],
                "animations": {"sit": "sit_NW", "seated": "typing_NW", "stand": "stand_NW"},
            },
        ],
        "action": {
            "idleLabel": "入座",
            "activeLabel": "起身",
            "status": "production-art 分层场景 + 透明动作帧",
            "targetAnchor": "seat_left_console",
            "targetMode": "typing_control",
            "returnAnchor": "walk_a",
        },
        "anchors": anchors,
        "walkPath": ["walk_a", "walk_b", "walk_c", "walk_d", "seat_left_console"],
        "people": [
            {
                "id": "lead",
                "kind": "female_01",
                "anchor": "seat_left_console",
                "mode": "typing_control",
                "z": 40,
                "interactive": True,
                "initialPhase": "seated",
            },
        ],
    }


def build_scene() -> None:
    SCENE.mkdir(parents=True, exist_ok=True)
    base = fit_scene(Image.open(SRC / "office-master.png").convert("RGB"))
    base.save(SCENE / "office_base.png")
    build_shadow().save(SCENE / "office_shadow.png")
    build_foreground(base).save(SCENE / "office_foreground.png")
    build_occluders(base)
    build_glass().save(SCENE / "office_glass.png")
    build_walkable_mask().save(SCENE / "walkable_mask.png")
    build_depth_map().save(SCENE / "depth_map.png")
    build_top_view_control().save(SCENE / "top_view_control.png")
    manifest = scene_manifest()
    (SCENE / "scene.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "anchors.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def write_asset_manifest() -> None:
    files = []
    for path in sorted(OUT.rglob("*")):
        if path.is_file():
            files.append(path.relative_to(OUT).as_posix())
    manifest = {
        "project": "aigc-studio-dashboard",
        "root": "public/assets/production-art",
        "scene": "scene/scene.json",
        "characters": ["female_01", "male_01"],
        "files": files,
        "notes": [
            "Final scene images are annotation-free except top_view_control.png.",
            "Seat occluders are split into scene/occluders/*.png and referenced from scene.json.",
            "sit/stand frames are generated from independent four-direction transition sheets in public/assets/final-art/.",
        ],
    }
    (OUT / "asset-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "README.md").write_text(
        "# Production Art Pack\n\n"
        "Generated from `public/assets/final-art/office-master.png` and the character alpha sheets.\n"
        "`scene/top_view_control.png` is control-only; do not render it in the final page.\n",
        encoding="utf-8",
    )


def validate_outputs() -> None:
    for name in (
        "office_base.png",
        "office_shadow.png",
        "office_foreground.png",
        "office_glass.png",
        "walkable_mask.png",
        "depth_map.png",
        "top_view_control.png",
        "scene.json",
    ):
        path = SCENE / name
        assert path.exists(), f"missing {path}"
        if path.suffix == ".png":
            assert Image.open(path).size == SCENE_SIZE, f"bad scene size: {path}"
    for name in OCCLUDER_SPECS:
        path = SCENE / "occluders" / f"{name}.png"
        assert path.exists(), f"missing {path}"
        assert Image.open(path).size == SCENE_SIZE, f"bad occluder size: {path}"

    for character_id in ("female_01", "male_01"):
        character_dir = CHARACTERS / character_id
        assert (character_dir / "master" / "threeview.png").exists()
        assert (character_dir / "master" / "detail_crops.png").exists()
        meta = json.loads((character_dir / "sprite_meta.json").read_text(encoding="utf-8"))
        assert meta["assetStatus"]["sit"] == "redrawn_independent_four_direction_transition_sheets"
        assert meta["assetStatus"]["stand"] == "redrawn_independent_four_direction_transition_sheets"
        for action, count in meta["actions"].items():
            for direction in meta["directions"]:
                anchor = meta["anchors"][f"{action}_{direction}"]
                if action in {"sit", "stand"}:
                    assert len(anchor["perFrameOrigins"]) == count, f"missing per-frame origins: {character_id} {action}_{direction}"
                frames = sorted((character_dir / "sprites" / f"{action}_{direction}").glob("*.png"))
                assert len(frames) == count, f"{character_id} {action}_{direction} has {len(frames)} frames"
                for frame in frames:
                    image = Image.open(frame)
                    assert image.mode == "RGBA", f"not transparent png: {frame}"
                    assert image.size == FRAME_SIZE, f"bad frame size: {frame}"


def main() -> None:
    target = OUT.resolve()
    expected_parent = (ROOT / "public" / "assets").resolve()
    if expected_parent not in target.parents:
        raise RuntimeError(f"refusing to delete unexpected output path: {target}")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    build_scene()
    build_character("female")
    build_character("male")
    write_asset_manifest()
    validate_outputs()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
