from __future__ import annotations

import argparse
from pathlib import Path

from common import JsonObject, print_json, tool_result, write_json
from frame_sampler import parse_times, sample_frames
from video_probe import probe_video

TOOL = "reference_video_analyzer"


def analyze_reference_video(
    video: Path,
    output_dir: Path,
    frame_count: int = 6,
    times: str | None = None,
) -> JsonObject:
    probed = probe_video(video)
    duration = probed["summary"]["duration_seconds"]
    if duration is None:
        raise RuntimeError("Cannot analyze a video without a known duration.")
    sample_times = parse_times(times, float(duration), frame_count)
    frames = sample_frames(video, output_dir / "keyframes", sample_times)
    analysis = {
        "video_path": str(video),
        "probe_summary": probed["summary"],
        "keyframes": [str(path) for path in frames],
        "sample_times": sample_times,
        "transcript": None,
        "transcript_status": "not_configured",
        "scene_list": [
            {
                "scene_id": "scene_001",
                "start_seconds": 0.0,
                "end_seconds": duration,
                "method": "single_scene_placeholder",
            }
        ],
    }
    write_json(output_dir / "analysis.json", analysis)
    return analysis


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze a reference video locally.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--frame-count", type=int, default=6)
    parser.add_argument("--times", default=None, help="Comma-separated seconds.")
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    inputs = {
        "input": str(args.input),
        "output_dir": str(args.output_dir),
        "frame_count": args.frame_count,
        "times": args.times,
    }
    try:
        analysis = analyze_reference_video(
            args.input, args.output_dir, args.frame_count, args.times
        )
        result = tool_result(TOOL, True, inputs=inputs, outputs={"analysis": analysis})
    except Exception as exc:
        result = tool_result(TOOL, False, inputs=inputs, error=str(exc))

    if args.output:
        write_json(args.output, result)
    print_json(result)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
