from __future__ import annotations

import importlib
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "scripts" / "tools"
sys.path.insert(0, str(TOOLS_DIR))


def test_video_probe_summarizes_streams() -> None:
    video_probe = importlib.import_module("video_probe")

    summary = video_probe.summarize_probe(
        {
            "format": {"duration": "2.5", "size": "1234", "format_name": "mov,mp4"},
            "streams": [
                {
                    "codec_type": "video",
                    "codec_name": "h264",
                    "width": 1920,
                    "height": 1080,
                    "avg_frame_rate": "30000/1001",
                },
                {
                    "codec_type": "audio",
                    "codec_name": "aac",
                    "sample_rate": "48000",
                    "channels": 2,
                },
            ],
        }
    )

    assert summary["duration_seconds"] == 2.5
    assert summary["size_bytes"] == 1234
    assert summary["video"]["fps"] == 30000 / 1001
    assert summary["audio"]["sample_rate"] == 48000


def test_frame_sampler_default_times_use_review_ratios() -> None:
    frame_sampler = importlib.import_module("frame_sampler")

    assert frame_sampler.default_sample_times(10.0, 4) == [1.0, 3.5, 6.5, 9.0]


def test_asset_resolver_registers_manifest(tmp_path: Path) -> None:
    asset_resolver = importlib.import_module("asset_resolver")
    source = tmp_path / "source.txt"
    dest = tmp_path / "assets"
    manifest = tmp_path / "manifest.json"
    source.write_text("hello", encoding="utf-8")

    outputs = asset_resolver.resolve_asset(str(source), dest, "text", manifest)

    record = outputs["record"]
    assert record["asset_type"] == "text"
    assert record["status"] == "frozen"
    assert Path(record["path"]).exists()
    assert record["asset_id"].startswith("text_")
    assert "hello" == Path(record["path"]).read_text(encoding="utf-8")


def test_ffmpeg_edit_builds_trim_command() -> None:
    ffmpeg_edit = importlib.import_module("ffmpeg_edit")

    assert ffmpeg_edit.trim_command(Path("in.mp4"), Path("out.mp4"), 1.5, 3.0) == [
        "ffmpeg",
        "-y",
        "-ss",
        "1.5",
        "-i",
        "in.mp4",
        "-t",
        "3.0",
        "-c",
        "copy",
        "out.mp4",
    ]


def test_delivery_qc_reports_duration_and_audio_issues() -> None:
    delivery_qc = importlib.import_module("delivery_qc")

    issues = delivery_qc.evaluate(
        {
            "duration_seconds": 8.0,
            "size_bytes": 100,
            "has_video": True,
            "has_audio": False,
            "video": {"width": 1280, "height": 720},
        },
        expect_duration=10.0,
        duration_tolerance=0.5,
        expect_width=1920,
        expect_height=1080,
        require_audio=True,
    )

    assert "missing audio stream" in issues
    assert "width 1280 != 1920" in issues
    assert "height 720 != 1080" in issues
    assert any(issue.startswith("duration 8.000s outside expected") for issue in issues)

