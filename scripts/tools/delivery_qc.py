from __future__ import annotations

import argparse
from pathlib import Path

from common import JsonObject, print_json, tool_result, write_json
from video_probe import probe_video

TOOL = "delivery_qc"


def evaluate(
    summary: JsonObject,
    *,
    expect_duration: float | None = None,
    duration_tolerance: float = 0.5,
    expect_width: int | None = None,
    expect_height: int | None = None,
    require_audio: bool = False,
    require_video: bool = True,
) -> list[str]:
    issues: list[str] = []
    if require_video and not summary["has_video"]:
        issues.append("missing video stream")
    if require_audio and not summary["has_audio"]:
        issues.append("missing audio stream")
    duration = summary["duration_seconds"]
    if expect_duration is not None:
        if duration is None:
            issues.append("missing duration")
        elif abs(float(duration) - expect_duration) > duration_tolerance:
            issues.append(
                f"duration {duration:.3f}s outside expected {expect_duration:.3f}s "
                f"+/- {duration_tolerance:.3f}s"
            )
    video = summary["video"]
    if expect_width is not None and video["width"] != expect_width:
        issues.append(f"width {video['width']} != {expect_width}")
    if expect_height is not None and video["height"] != expect_height:
        issues.append(f"height {video['height']} != {expect_height}")
    if summary["size_bytes"] in (None, 0):
        issues.append("empty or unknown file size")
    return issues


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run basic final media QC checks.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--expect-duration", type=float, default=None)
    parser.add_argument("--duration-tolerance", type=float, default=0.5)
    parser.add_argument("--expect-width", type=int, default=None)
    parser.add_argument("--expect-height", type=int, default=None)
    parser.add_argument("--require-audio", action="store_true")
    parser.add_argument("--allow-no-video", action="store_true")
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    inputs = {
        "input": str(args.input),
        "expect_duration": args.expect_duration,
        "duration_tolerance": args.duration_tolerance,
        "expect_width": args.expect_width,
        "expect_height": args.expect_height,
        "require_audio": args.require_audio,
        "allow_no_video": args.allow_no_video,
    }
    try:
        summary = probe_video(args.input)["summary"]
        issues = evaluate(
            summary,
            expect_duration=args.expect_duration,
            duration_tolerance=args.duration_tolerance,
            expect_width=args.expect_width,
            expect_height=args.expect_height,
            require_audio=args.require_audio,
            require_video=not args.allow_no_video,
        )
        outputs = {"passed": not issues, "issues": issues, "summary": summary}
        result = tool_result(TOOL, not issues, inputs=inputs, outputs=outputs)
    except Exception as exc:
        result = tool_result(TOOL, False, inputs=inputs, error=str(exc))

    if args.output:
        write_json(args.output, result)
    print_json(result)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

