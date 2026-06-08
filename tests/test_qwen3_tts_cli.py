from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

from pytest import MonkeyPatch


def load_script() -> ModuleType:
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "qwen3_tts.py"
    spec = importlib.util.spec_from_file_location("qwen3_tts_script", script_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_parse_args_uses_mlx_custom_voice_default() -> None:
    script = load_script()

    args = script.parse_args(["--text", "hello"])

    assert args.text == "hello"
    assert args.mode == "auto"
    assert args.backend == "auto"
    assert args.model is None
    assert args.output == Path("project/run/qwen3-tts/output.wav")


def test_resolve_backend_prefers_torch_outside_apple_silicon(monkeypatch: MonkeyPatch) -> None:
    script = load_script()

    monkeypatch.setattr(script.sys, "platform", "win32")
    monkeypatch.setattr(script.platform, "machine", lambda: "AMD64")

    assert script.resolve_backend("auto") == "torch"


def test_resolve_model_uses_backend_specific_defaults() -> None:
    script = load_script()

    assert script.resolve_model(None, "mlx") == "mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-bf16"
    assert script.resolve_model(None, "torch") == "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"


def test_build_generation_kwargs_maps_cli_names_to_backends() -> None:
    script = load_script()
    args = script.parse_args(
        [
            "--text",
            "hello",
            "--temperature",
            "0.7",
            "--top-p",
            "0.9",
            "--max-tokens",
            "128",
        ]
    )

    assert script.build_mlx_generation_kwargs(args) == {
        "max_tokens": 128,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 0.9,
        "repetition_penalty": 1.05,
        "verbose": False,
        "stream": False,
        "streaming_interval": 2.0,
    }
    assert script.build_torch_generation_kwargs(args) == {
        "max_new_tokens": 128,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 0.9,
        "repetition_penalty": 1.05,
    }


def test_infer_audio_format_defaults_to_wav_for_extensionless_path() -> None:
    script = load_script()

    assert script.infer_audio_format(Path("project/run/qwen3-tts/output")) == "wav"
