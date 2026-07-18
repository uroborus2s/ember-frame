from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from common import JsonObject, print_json, run_command, tool_result, write_json

TOOL = "video_probe"


def parse_rate(value: str | None) -> float | None:
    if not value or value == "0/0":
        return None
    if "/" not in value:
        return float(value)
    numerator, denominator = value.split("/", 1)
    den = float(denominator)
    if den == 0:
        return None
    return float(numerator) / den


def parse_float(value: Any) -> float | None:
    if value in (None, "N/A"):
        return None
    return float(value)


def summarize_probe(raw: JsonObject) -> JsonObject:
    streams = raw.get("streams", [])
    video_streams = [s for s in streams if s.get("codec_type") == "video"]
    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]
    fmt = raw.get("format", {})
    first_video = video_streams[0] if video_streams else {}
    first_audio = audio_streams[0] if audio_streams else {}

    return {
        "duration_seconds": parse_float(fmt.get("duration")),
        "size_bytes": int(fmt["size"]) if fmt.get("size") not in (None, "N/A") else None,
        "format_name": fmt.get("format_name"),
        "has_video": bool(video_streams),
        "has_audio": bool(audio_streams),
        "video": {
            "codec": first_video.get("codec_name"),
            "width": first_video.get("width"),
            "height": first_video.get("height"),
            "fps": parse_rate(first_video.get("avg_frame_rate")),
            "stream_count": len(video_streams),
        },
        "audio": {
            "codec": first_audio.get("codec_name"),
            "sample_rate": int(first_audio["sample_rate"])
            if first_audio.get("sample_rate") not in (None, "N/A")
            else None,
            "channels": first_audio.get("channels"),
            "stream_count": len(audio_streams),
        },
    }


def ffprobe(path: Path) -> JsonObject:
    completed = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(path),
        ]
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "ffprobe failed")
    data = json.loads(completed.stdout)
    if not isinstance(data, dict):
        raise RuntimeError("ffprobe returned non-object JSON")
    return data


def probe_video(path: Path) -> JsonObject:
    raw = ffprobe(path)
    return {"raw": raw, "summary": summarize_probe(raw)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Probe a media file with ffprobe.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--raw", action="store_true", help="Include raw ffprobe JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        data = probe_video(args.input)
        outputs: JsonObject = {"summary": data["summary"]}
        if args.raw:
            outputs["raw"] = data["raw"]
        result = tool_result(TOOL, True, inputs={"input": str(args.input)}, outputs=outputs)
    except Exception as exc:
        result = tool_result(TOOL, False, inputs={"input": str(args.input)}, error=str(exc))

    if args.output:
        write_json(args.output, result)
    print_json(result)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
