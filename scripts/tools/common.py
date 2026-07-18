from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

JsonObject = dict[str, Any]


def tool_result(
    tool: str,
    success: bool,
    *,
    inputs: JsonObject | None = None,
    outputs: JsonObject | None = None,
    metadata: JsonObject | None = None,
    error: str | None = None,
) -> JsonObject:
    return {
        "success": success,
        "tool": tool,
        "input": inputs or {},
        "outputs": outputs or {},
        "metadata": metadata or {},
        "error": error,
    }


def write_json(path: Path, data: JsonObject) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def print_json(data: JsonObject) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def run_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=False, capture_output=True, text=True)

