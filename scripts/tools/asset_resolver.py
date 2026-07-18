from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import shutil
import urllib.parse
import urllib.request
from pathlib import Path

from common import JsonObject, print_json, tool_result, write_json

TOOL = "asset_resolver"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))


def asset_id_for(asset_type: str, digest: str) -> str:
    return f"{asset_type}_{digest[:12]}"


def freeze_source(source: str, dest_dir: Path, filename: str | None = None) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    if is_url(source):
        name = filename or Path(urllib.parse.urlparse(source).path).name or "downloaded_asset"
        output = dest_dir / name
        urllib.request.urlretrieve(source, output)
        return output

    source_path = Path(source)
    if not source_path.exists():
        raise FileNotFoundError(source)
    output = dest_dir / (filename or source_path.name)
    if source_path.resolve() != output.resolve():
        shutil.copy2(source_path, output)
    return output


def load_manifest(path: Path) -> JsonObject:
    if not path.exists():
        return {"assets": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"Manifest is not a JSON object: {path}")
    return data


def upsert_asset(manifest: JsonObject, record: JsonObject) -> JsonObject:
    assets = [
        item for item in manifest.get("assets", []) if item.get("asset_id") != record["asset_id"]
    ]
    assets.append(record)
    manifest["assets"] = sorted(assets, key=lambda item: item["asset_id"])
    return manifest


def build_record(asset_id: str, asset_type: str, source: str, frozen_path: Path) -> JsonObject:
    digest = sha256_file(frozen_path)
    return {
        "asset_id": asset_id,
        "asset_type": asset_type,
        "source": source,
        "path": str(frozen_path),
        "sha256": digest,
        "size_bytes": frozen_path.stat().st_size,
        "mime_type": mimetypes.guess_type(frozen_path.name)[0],
        "status": "frozen",
    }


def resolve_asset(
    source: str,
    dest_dir: Path,
    asset_type: str,
    manifest_path: Path,
    asset_id: str | None = None,
    filename: str | None = None,
) -> JsonObject:
    frozen_path = freeze_source(source, dest_dir, filename)
    digest = sha256_file(frozen_path)
    resolved_id = asset_id or asset_id_for(asset_type, digest)
    record = build_record(resolved_id, asset_type, source, frozen_path)
    manifest = upsert_asset(load_manifest(manifest_path), record)
    write_json(manifest_path, manifest)
    return {"record": record, "manifest_path": str(manifest_path)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Freeze a media asset and register it in a manifest."
    )
    parser.add_argument("source", help="Local path or http(s) URL.")
    parser.add_argument("--dest-dir", type=Path, required=True)
    parser.add_argument("--asset-type", default="asset")
    parser.add_argument("--asset-id", default=None)
    parser.add_argument("--filename", default=None)
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    manifest_path = args.manifest or args.dest_dir / "asset-manifest.json"
    inputs = {
        "source": args.source,
        "dest_dir": str(args.dest_dir),
        "asset_type": args.asset_type,
        "asset_id": args.asset_id,
        "filename": args.filename,
        "manifest": str(manifest_path),
    }
    try:
        outputs = resolve_asset(
            args.source,
            args.dest_dir,
            args.asset_type,
            manifest_path,
            args.asset_id,
            args.filename,
        )
        result = tool_result(TOOL, True, inputs=inputs, outputs=outputs)
    except Exception as exc:
        result = tool_result(TOOL, False, inputs=inputs, error=str(exc))

    if args.output:
        write_json(args.output, result)
    print_json(result)
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
