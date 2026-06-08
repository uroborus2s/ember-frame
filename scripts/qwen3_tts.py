"""Generate speech with Qwen3-TTS through a platform-specific backend."""

from __future__ import annotations

import argparse
import platform
import sys
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any, Literal, cast

DEFAULT_MLX_MODEL = "mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-bf16"
DEFAULT_TORCH_MODEL = "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"
DEFAULT_OUTPUT = Path("project/run/qwen3-tts/output.wav")

Backend = Literal["auto", "mlx", "torch"]
ResolvedBackend = Literal["mlx", "torch"]
Mode = Literal["auto", "custom-voice", "voice-design", "base", "voice-clone"]


@dataclass(frozen=True)
class AudioResult:
    audio: Any
    sample_rate: int


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate an audio file with Qwen3-TTS.",
    )
    parser.add_argument("--text", required=True, help="Text to synthesize.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output audio path. Defaults to {DEFAULT_OUTPUT}.",
    )
    parser.add_argument(
        "--backend",
        choices=["auto", "mlx", "torch"],
        default="auto",
        help="auto uses MLX on Apple Silicon macOS and torch elsewhere.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model repo id or local model directory. Defaults by backend.",
    )
    parser.add_argument(
        "--mode",
        choices=["auto", "custom-voice", "voice-design", "base", "voice-clone"],
        default="auto",
        help="Generation API to call. auto routes by selected backend/model.",
    )
    parser.add_argument(
        "--language",
        default="auto",
        help="Language accepted by Qwen3-TTS, for example auto, chinese, english.",
    )
    parser.add_argument(
        "--voice",
        default="Vivian",
        help="Speaker/voice name for Base or CustomVoice models.",
    )
    parser.add_argument(
        "--instruct",
        default=None,
        help="Style instruction for CustomVoice, or voice description for VoiceDesign.",
    )
    parser.add_argument("--ref-audio", default=None, help="Reference audio for voice clone.")
    parser.add_argument("--ref-text", default=None, help="Reference audio transcript.")
    parser.add_argument(
        "--x-vector-only",
        action="store_true",
        help="Torch Base voice-clone mode only: use speaker embedding without ref text.",
    )
    parser.add_argument("--speed", type=float, default=1.0, help="Speech speed multiplier.")
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--temperature", type=float, default=0.9)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--repetition-penalty", type=float, default=1.05)
    parser.add_argument("--stream", action="store_true", help="Stream generation internally.")
    parser.add_argument("--streaming-interval", type=float, default=2.0)
    parser.add_argument("--verbose", action="store_true", help="Print backend generation stats.")
    parser.add_argument(
        "--device",
        default="auto",
        help="Torch backend only: auto, cpu, cuda:0, or another Transformers device_map value.",
    )
    parser.add_argument(
        "--dtype",
        choices=["auto", "bfloat16", "float16", "float32"],
        default="auto",
        help="Torch backend only: dtype for model loading.",
    )
    parser.add_argument(
        "--flash-attn",
        action="store_true",
        help="Torch backend only: enable FlashAttention 2 when installed and supported.",
    )
    return parser


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    return build_parser().parse_args(argv)


def resolve_backend(backend: Backend) -> ResolvedBackend:
    if backend != "auto":
        return backend
    if sys.platform == "darwin" and platform.machine().lower() == "arm64":
        return "mlx"
    return "torch"


def resolve_model(model: str | None, backend: ResolvedBackend) -> str:
    if model:
        return model
    if backend == "mlx":
        return DEFAULT_MLX_MODEL
    return DEFAULT_TORCH_MODEL


def build_mlx_generation_kwargs(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "top_k": args.top_k,
        "top_p": args.top_p,
        "repetition_penalty": args.repetition_penalty,
        "verbose": args.verbose,
        "stream": args.stream,
        "streaming_interval": args.streaming_interval,
    }


def build_torch_generation_kwargs(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "max_new_tokens": args.max_tokens,
        "temperature": args.temperature,
        "top_k": args.top_k,
        "top_p": args.top_p,
        "repetition_penalty": args.repetition_penalty,
    }


def synthesize_with_mlx(args: argparse.Namespace, model_id: str) -> list[AudioResult]:
    mlx_utils = cast(Any, import_module("mlx_audio.tts.utils"))

    model = mlx_utils.load_model(model_id)
    generation_kwargs = build_mlx_generation_kwargs(args)
    mode: Mode = args.mode

    if mode == "custom-voice":
        results = model.generate_custom_voice(
            text=args.text,
            speaker=args.voice,
            language=args.language,
            instruct=args.instruct,
            **generation_kwargs,
        )
    elif mode == "voice-design":
        if not args.instruct:
            raise ValueError("--instruct is required when --mode voice-design.")
        results = model.generate_voice_design(
            text=args.text,
            language=args.language,
            instruct=args.instruct,
            **generation_kwargs,
        )
    else:
        results = model.generate(
            text=args.text,
            voice=args.voice,
            instruct=args.instruct,
            lang_code=args.language,
            ref_audio=args.ref_audio,
            ref_text=args.ref_text,
            speed=args.speed,
            **generation_kwargs,
        )

    return [AudioResult(result.audio, int(result.sample_rate)) for result in results]


def resolve_torch_device(device: str) -> str:
    if device != "auto":
        return device

    torch = cast(Any, import_module("torch"))

    if torch.cuda.is_available():
        return "cuda:0"
    return "cpu"


def resolve_torch_dtype(dtype: str, device: str) -> Any:
    torch = cast(Any, import_module("torch"))

    if dtype == "auto":
        return torch.bfloat16 if device.startswith("cuda") else torch.float32

    dtype_map = {
        "bfloat16": torch.bfloat16,
        "float16": torch.float16,
        "float32": torch.float32,
    }
    return dtype_map[dtype]


def synthesize_with_torch(args: argparse.Namespace, model_id: str) -> list[AudioResult]:
    qwen_tts = cast(Any, import_module("qwen_tts"))

    device = resolve_torch_device(args.device)
    dtype = resolve_torch_dtype(args.dtype, device)
    load_kwargs: dict[str, Any] = {
        "device_map": device,
        "dtype": dtype,
    }
    if args.flash_attn:
        load_kwargs["attn_implementation"] = "flash_attention_2"

    model = qwen_tts.Qwen3TTSModel.from_pretrained(model_id, **load_kwargs)
    generation_kwargs = build_torch_generation_kwargs(args)
    mode: Mode = args.mode

    if mode in ("auto", "custom-voice"):
        wavs, sample_rate = model.generate_custom_voice(
            text=args.text,
            language=args.language,
            speaker=args.voice,
            instruct=args.instruct,
            **generation_kwargs,
        )
    elif mode == "voice-design":
        if not args.instruct:
            raise ValueError("--instruct is required when --mode voice-design.")
        wavs, sample_rate = model.generate_voice_design(
            text=args.text,
            language=args.language,
            instruct=args.instruct,
            **generation_kwargs,
        )
    else:
        if not args.ref_audio:
            raise ValueError("--ref-audio is required when --mode base or voice-clone.")
        if not args.x_vector_only and not args.ref_text:
            raise ValueError("--ref-text is required unless --x-vector-only is set.")
        wavs, sample_rate = model.generate_voice_clone(
            text=args.text,
            language=args.language,
            ref_audio=args.ref_audio,
            ref_text=args.ref_text,
            x_vector_only_mode=args.x_vector_only,
            **generation_kwargs,
        )

    return [AudioResult(wav, int(sample_rate)) for wav in wavs]


def synthesize(args: argparse.Namespace) -> tuple[ResolvedBackend, list[AudioResult]]:
    backend = resolve_backend(args.backend)
    model_id = resolve_model(args.model, backend)

    if backend == "mlx":
        return backend, synthesize_with_mlx(args, model_id)
    return backend, synthesize_with_torch(args, model_id)


def infer_audio_format(path: Path) -> str:
    suffix = path.suffix.lstrip(".").lower()
    return suffix or "wav"


def audio_to_numpy(audio: Any) -> Any:
    import numpy as np

    if hasattr(audio, "__array__"):
        return np.asarray(audio)
    if hasattr(audio, "tolist"):
        return np.array(audio.tolist())
    return np.array(audio)


def write_results(path: Path, results: list[AudioResult]) -> None:
    if not results:
        raise RuntimeError("Qwen3-TTS returned no audio results.")

    sample_rates = {result.sample_rate for result in results}
    if len(sample_rates) != 1:
        raise RuntimeError(f"Cannot join results with different sample rates: {sample_rates}")

    import numpy as np

    chunks = [audio_to_numpy(result.audio) for result in results]
    audio = np.concatenate(chunks, axis=0) if len(chunks) > 1 else chunks[0]

    path.parent.mkdir(parents=True, exist_ok=True)
    audio_format = infer_audio_format(path)
    try:
        mlx_audio_io = cast(Any, import_module("mlx_audio.audio_io"))
    except ImportError:
        soundfile = cast(Any, import_module("soundfile"))

        soundfile.write(path, audio, sample_rates.pop(), format=audio_format)
    else:
        mlx_audio_io.write(path, audio, sample_rates.pop(), format=audio_format)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    backend, results = synthesize(args)
    write_results(args.output, results)
    print(f"Wrote {args.output} with {backend} backend")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
