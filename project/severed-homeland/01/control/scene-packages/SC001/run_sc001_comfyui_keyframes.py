#!/usr/bin/env python3
"""Run SC001 r001-r004 keyframe candidates through a minimal ComfyUI API workflow."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCENE_DIR = ROOT / "control" / "scene-packages" / "SC001"
COMFY = "http://127.0.0.1:8188"
CHECKPOINT = "v2-1_768-ema-pruned.safetensors"
RUN_REPORT = ROOT / "production" / "comfyui-sc001-keyframe-run.json"

TASKS = [
    {
        "slot": "r001",
        "shot_id": "SC001-SH001",
        "source_reference": "assets/reference-frames/r001e01.png",
        "camera": "control/scene-packages/SC001/shot-guides/r001_camera.png",
        "depth": "control/scene-packages/SC001/depth/r001_depth.png",
        "lineart": "control/scene-packages/SC001/lineart/r001_lineart.png",
        "output": "assets/director-room/shots/SC001-SH001/candidates/r001e01.candidate.png",
        "seed": 101001,
        "positive": (
            "cinematic dark fantasy production keyframe, low centered exterior siege establishing shot, "
            "same blackstone fortress wall and same timber iron gate, C020/C021/E01_C020 multi-branch beast "
            "troops, bonded companion siege beasts and siege engine "
            "pressing through blizzard along one central axis, wall-top defender spear silhouettes, "
            "cold moonlit snow, sharp readable gate geometry, epic pressure, painterly realism"
        ),
        "negative": (
            "second wall, second gate, interior city view, attackers inside the wall, visible alarm bell close up, "
            "wrong banner, flat grey fog, clean modern architecture, text, logo, watermark, distorted perspective"
        ),
    },
    {
        "slot": "r002",
        "shot_id": "SC001-SH001",
        "source_reference": "assets/reference-frames/r002e01.png",
        "camera": "control/scene-packages/SC001/shot-guides/r002_camera.png",
        "depth": "control/scene-packages/SC001/depth/r002_depth.png",
        "lineart": "control/scene-packages/SC001/lineart/r002_lineart.png",
        "output": "assets/director-room/shots/SC001-SH001/candidates/r002e01.candidate.png",
        "seed": 101002,
        "positive": (
            "cinematic dark fantasy production keyframe, closer exterior axis at the same fortress gate, "
            "C020/C021/E01_C020 beast siege line and bonded companion beast pressure, iron wrapped siege horn "
            "slamming the timber iron gate, snow blast, ice splinters, old wood chips, "
            "shaking gate bars as bright focal detail, same blackstone wall, wall-top defender silhouettes, "
            "cold violent impact, painterly realism"
        ),
        "negative": (
            "camera turn, wall pass through, city interior, second gate, impact away from gate, clean heroic pose, "
            "modern metal door, text, logo, watermark, flat fog, distorted gate scale"
        ),
    },
    {
        "slot": "r003",
        "shot_id": "SC001-SH002",
        "source_reference": "assets/reference-frames/r003e01.png",
        "camera": "control/scene-packages/SC001/shot-guides/r003_camera.png",
        "depth": "control/scene-packages/SC001/depth/r003_depth.png",
        "lineart": "control/scene-packages/SC001/lineart/r003_lineart.png",
        "output": "assets/director-room/shots/SC001-SH002/candidates/r003e01.candidate.png",
        "seed": 101003,
        "positive": (
            "cinematic dark fantasy production keyframe, tight medium gatehouse interior, broken spear in foreground "
            "sliding through dirty snow mud, E01_C024A young grey wall soldier knocked down alive by gate-impact "
            "aftershock, half-open squinting eyes, visible cold breath, one splayed hand bracing in snow mud, "
            "bent knee and slipping boot, same five-thousand-year-old Zhaoming old-empire oxidized metal "
            "alarm bell swinging under timber frame in background, diagonal chain, broken unreadable sun-moon "
            "astrolabe emblem fragments derived from P016 only, cold battle pressure outside as blizzard and smoke only, layered depth, painterly realism"
        ),
        "negative": (
            "heroic front face, bell bracing pose, changed bell frame, open exterior battlefield, second wall, "
            "soldier dead, closed corpse eyes, limp neck, slack dead face, blood pool, soldier standing, clean armor, "
            "complete clean emblem, P018 beast emblem on the bell, ivory or bone bell surface, "
            "houses, warm windows, city streets, city towers, text, logo, watermark, flat composition, missing bell"
        ),
    },
    {
        "slot": "r004",
        "shot_id": "SC001-SH003",
        "source_reference": "assets/reference-frames/r004e01.png",
        "camera": "control/scene-packages/SC001/shot-guides/r004_camera.png",
        "depth": "control/scene-packages/SC001/depth/r004_depth.png",
        "lineart": "control/scene-packages/SC001/lineart/r004_lineart.png",
        "output": "assets/director-room/shots/SC001-SH003/candidates/r004e01.candidate.png",
        "seed": 101004,
        "positive": (
            "cinematic dark fantasy production keyframe, rear three quarter medium close shot inside the same "
            "gatehouse parapet, Xue Linqiang pressing the blackstone parapet and facing outward, cracked frozen hand, "
            "coarse wall scarf, old armor plates, half dark side profile, same five-thousand-year-old Zhaoming "
            "old-empire oxidized metal alarm bell swinging in background with broken unreadable sun-moon astrolabe "
            "emblem fragments derived from P016 only, exterior below the parapet is only blizzard, smoke, "
            "C020/C021/E01_C020 multi-branch beast soldiers, bonded companion beasts, siege mammoths, rhinos, "
            "oxen and siege equipment pressure, painterly realism"
        ),
        "negative": (
            "clean war god styling, heroic low angle, missing background bell, young soldier standing, beast attackers "
            "inside gatehouse, second wall, second gate, houses, warm windows, city streets, city towers, complete clean "
            "emblem, P018 beast emblem on the bell, ivory or bone bell surface, human army outside, generic single-species "
            "orc horde, ownerless monster pack, modern costume, text, logo, watermark, distorted face"
        ),
    },
]


def http_json(path: str, data: dict | None = None, timeout: int = 30) -> dict:
    body = None
    headers = {}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(f"{COMFY}{path}", data=body, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = response.read()
    return json.loads(payload.decode("utf-8")) if payload else {}


def upload_image(path: Path, upload_name: str) -> str:
    boundary = f"----codex-{uuid.uuid4().hex}"
    content = path.read_bytes()
    fields = [
        (b"overwrite", b"true"),
        (b"type", b"input"),
    ]
    parts: list[bytes] = []
    for name, value in fields:
        parts.append(b"--" + boundary.encode())
        parts.append(b'Content-Disposition: form-data; name="' + name + b'"')
        parts.append(b"")
        parts.append(value)
    parts.append(b"--" + boundary.encode())
    disposition = (
        f'Content-Disposition: form-data; name="image"; filename="{upload_name}"'
    ).encode("utf-8")
    parts.append(disposition)
    parts.append(b"Content-Type: image/png")
    parts.append(b"")
    parts.append(content)
    parts.append(b"--" + boundary.encode() + b"--")
    parts.append(b"")
    body = b"\r\n".join(parts)
    request = urllib.request.Request(
        f"{COMFY}/upload/image",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result["name"]


def build_prompt(task: dict, uploaded_image: str) -> dict:
    return {
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {"ckpt_name": CHECKPOINT},
        },
        "2": {
            "class_type": "LoadImage",
            "inputs": {"image": uploaded_image},
        },
        "3": {
            "class_type": "ImageScale",
            "inputs": {
                "image": ["2", 0],
                "upscale_method": "lanczos",
                "width": 768,
                "height": 432,
                "crop": "center",
            },
        },
        "4": {
            "class_type": "VAEEncode",
            "inputs": {"pixels": ["3", 0], "vae": ["1", 2]},
        },
        "5": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": task["positive"], "clip": ["1", 1]},
        },
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": task["negative"], "clip": ["1", 1]},
        },
        "7": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["1", 0],
                "seed": task["seed"],
                "steps": 24,
                "cfg": 7.0,
                "sampler_name": "euler",
                "scheduler": "normal",
                "positive": ["5", 0],
                "negative": ["6", 0],
                "latent_image": ["4", 0],
                "denoise": 0.68,
            },
        },
        "8": {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["7", 0], "vae": ["1", 2]},
        },
        "9": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["8", 0],
                "filename_prefix": f"severed_homeland_sc001/{task['slot']}",
            },
        },
    }


def wait_for_outputs(prompt_id: str, timeout: int = 600) -> list[dict]:
    deadline = time.time() + timeout
    while time.time() < deadline:
        history = http_json(f"/history/{prompt_id}", timeout=30)
        item = history.get(prompt_id)
        if item:
            outputs = []
            for node_output in item.get("outputs", {}).values():
                outputs.extend(node_output.get("images", []))
            if outputs:
                return outputs
            status = item.get("status", {})
            if status.get("completed") is False:
                messages = status.get("messages", [])
                raise RuntimeError(f"ComfyUI prompt failed: {messages}")
        time.sleep(2)
    raise TimeoutError(f"Timed out waiting for ComfyUI prompt {prompt_id}")


def download_output(image_info: dict, destination: Path) -> None:
    query = urllib.parse.urlencode(
        {
            "filename": image_info["filename"],
            "subfolder": image_info.get("subfolder", ""),
            "type": image_info.get("type", "output"),
        }
    )
    with urllib.request.urlopen(f"{COMFY}/view?{query}", timeout=60) as response:
        data = response.read()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


def validate_inputs() -> dict:
    stats = http_json("/system_stats", timeout=30)
    checkpoint_info = http_json("/object_info/CheckpointLoaderSimple", timeout=30)
    controlnet_info = http_json("/object_info/ControlNetLoader", timeout=30)
    ckpt_choices = checkpoint_info["CheckpointLoaderSimple"]["input"]["required"]["ckpt_name"][0]
    controlnet_choices = controlnet_info["ControlNetLoader"]["input"]["required"]["control_net_name"][0]
    preflight = {
        "system_stats": stats,
        "checkpoint_choices": ckpt_choices,
        "checkpoint_visible": CHECKPOINT in ckpt_choices,
        "required_checkpoint": CHECKPOINT,
        "controlnet_choices": controlnet_choices,
        "controlnet_available": bool(controlnet_choices),
    }
    for task in TASKS:
        for key in ["camera", "depth", "lineart", "source_reference"]:
            path = ROOT / task[key]
            if not path.exists():
                raise FileNotFoundError(path)
    return preflight


def main() -> None:
    run = {
        "version": "comfyui-sc001-keyframe-run-v1",
        "project": "severed-homeland",
        "episode_id": "01",
        "scene_id": "SC001",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "comfyui_endpoint": COMFY,
        "checkpoint": CHECKPOINT,
        "mode": "img2img_from_blender_camera_guides",
        "limitation": "ControlNet models are not installed, so depth and lineart are recorded but not connected as ControlNet inputs.",
        "results": [],
    }
    try:
        run["preflight"] = validate_inputs()
        if not run["preflight"]["checkpoint_visible"]:
            raise RuntimeError(f"Checkpoint not visible to ComfyUI: {CHECKPOINT}")
        for task in TASKS:
            upload_name = f"sc001_{task['slot']}_camera.png"
            uploaded = upload_image(ROOT / task["camera"], upload_name)
            prompt = build_prompt(task, uploaded)
            queued = http_json(
                "/prompt",
                {
                    "client_id": "codex-sc001-keyframes",
                    "prompt": prompt,
                },
                timeout=60,
            )
            prompt_id = queued["prompt_id"]
            outputs = wait_for_outputs(prompt_id)
            destination = ROOT / task["output"]
            download_output(outputs[0], destination)
            run["results"].append(
                {
                    "task_id": f"SC001_{task['slot'].upper()}_KEYFRAME_CANDIDATE",
                    "status": "generated",
                    "prompt_id": prompt_id,
                    "uploaded_camera_guide": uploaded,
                    "source_reference": task["source_reference"],
                    "control_inputs": {
                        "camera": task["camera"],
                        "depth": task["depth"],
                        "lineart": task["lineart"],
                    },
                    "output": task["output"],
                    "seed": task["seed"],
                    "workflow_note": "img2img camera guide; depth/lineart not connected because no ControlNet model is available",
                    "comfyui_output": outputs[0],
                }
            )
        run["status"] = "generated_with_limitations"
    except Exception as exc:
        run["status"] = "failed"
        run["error"] = repr(exc)
        raise
    finally:
        run["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        RUN_REPORT.parent.mkdir(parents=True, exist_ok=True)
        RUN_REPORT.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
