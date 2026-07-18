from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from common import JsonObject, print_json, run_command, tool_result, write_json

TOOL = "ffmpeg_edit"


def trim_command(input_path: Path, output_path: Path, start: float, duration: float) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-ss",
        str(start),
        "-i",
        str(input_path),
        "-t",
        str(duration),
        "-c",
        "copy",
        str(output_path),
    ]


def extract_audio_command(input_path: Path, output_path: Path) -> list[str]:
    return ["ffmpeg", "-y", "-i", str(input_path), "-vn", "-acodec", "copy", str(output_path)]


def concat_command(file_list: Path, output_path: Path) -> list[str]:
    return [
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(file_list),
        "-c",
        "copy",
        str(output_path),
    ]


def run_ffmpeg(args: list[str]) -> None:
    completed = run_command(args)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "ffmpeg failed")


def trim(input_path: Path, output_path: Path, start: float, duration: float) -> JsonObject:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = trim_command(input_path, output_path, start, duration)
    run_ffmpeg(command)
    return {"output": str(output_path), "command": command}


def extract_audio(input_path: Path, output_path: Path) -> JsonObject:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = extract_audio_command(input_path, output_path)
    run_ffmpeg(command)
    return {"output": str(output_path), "command": command}


def concat(inputs: list[Path], output_path: Path) -> JsonObject:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as file:
        list_path = Path(file.name)
        for input_path in inputs:
            file.write(f"file '{input_path.resolve().as_posix()}'\n")
    try:
        command = concat_command(list_path, output_path)
        run_ffmpeg(command)
    finally:
        list_path.unlink(missing_ok=True)
    return {"output": str(output_path), "command": command}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Small FFmpeg edit operations.")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    trim_parser = subparsers.add_parser("trim")
    trim_parser.add_argument("input", type=Path)
    trim_parser.add_argument("output", type=Path)
    trim_parser.add_argument("--start", type=float, default=0.0)
    trim_parser.add_argument("--duration", type=float, required=True)

    concat_parser = subparsers.add_parser("concat")
    concat_parser.add_argument("output", type=Path)
    concat_parser.add_argument("inputs", type=Path, nargs="+")

    audio_parser = subparsers.add_parser("extract-audio")
    audio_parser.add_argument("input", type=Path)
    audio_parser.add_argument("output", type=Path)

    parser.add_argument("--json-output", type=Path, default=None)
    return parser


def cli_inputs(args: argparse.Namespace) -> JsonObject:
    data = vars(args).copy()
    for key, value in list(data.items()):
        if isinstance(value, Path):
            data[key] = str(value)
        elif isinstance(value, list):
            data[key] = [str(item) if isinstance(item, Path) else item for item in value]
    return data


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    inputs = cli_inputs(args)
    try:
        if args.operation == "trim":
            outputs = trim(args.input, args.output, args.start, args.duration)
        elif args.operation == "concat":
            outputs = concat(args.inputs, args.output)
        else:
            outputs = extract_audio(args.input, args.output)
        result = tool_result(TOOL, True, inputs=inputs, outputs=outputs)
    except Exception as exc:
        result = tool_result(TOOL, False, inputs=inputs, error=str(exc))

    if args.json_output:
        write_json(args.json_output, result)
    print_json(result)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
