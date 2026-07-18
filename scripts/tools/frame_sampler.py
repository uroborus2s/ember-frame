from __future__ import annotations

import argparse
from pathlib import Path

from common import JsonObject, print_json, run_command, tool_result, write_json
from video_probe import probe_video

TOOL = "frame_sampler"


def default_sample_times(duration: float, count: int) -> list[float]:
    if count <= 0:
        raise ValueError("count must be positive")
    if count == 4:
        ratios = [0.10, 0.35, 0.65, 0.90]
    else:
        ratios = [(index + 1) / (count + 1) for index in range(count)]
    return [max(0.0, min(duration, duration * ratio)) for ratio in ratios]


def parse_times(value: str | None, duration: float, count: int) -> list[float]:
    if not value:
        return default_sample_times(duration, count)
    return [float(part.strip()) for part in value.split(",") if part.strip()]


def sample_frames(video: Path, output_dir: Path, times: list[float]) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    frames: list[Path] = []
    for index, seconds in enumerate(times, start=1):
        output = output_dir / f"frame_{index:03d}_{seconds:.2f}s.jpg"
        completed = run_command(
            [
                "ffmpeg",
                "-y",
                "-ss",
                f"{seconds:.3f}",
                "-i",
                str(video),
                "-frames:v",
                "1",
                "-q:v",
                "2",
                str(output),
            ]
        )
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip() or "ffmpeg frame sampling failed")
        frames.append(output)
    return frames


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sample still frames from a video.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--count", type=int, default=4)
    parser.add_argument("--times", default=None, help="Comma-separated seconds, overrides --count.")
    parser.add_argument("--output", type=Path, default=None, help="Optional JSON result path.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    inputs = {
        "input": str(args.input),
        "output_dir": str(args.output_dir),
        "count": args.count,
        "times": args.times,
    }
    try:
        probed = probe_video(args.input)
        duration = probed["summary"]["duration_seconds"]
        if duration is None:
            raise RuntimeError("Cannot sample frames without a known duration.")
        times = parse_times(args.times, float(duration), args.count)
        frames = sample_frames(args.input, args.output_dir, times)
        outputs: JsonObject = {"frames": [str(path) for path in frames], "times": times}
        result = tool_result(TOOL, True, inputs=inputs, outputs=outputs)
    except Exception as exc:
        result = tool_result(TOOL, False, inputs=inputs, error=str(exc))

    if args.output:
        write_json(args.output, result)
    print_json(result)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

