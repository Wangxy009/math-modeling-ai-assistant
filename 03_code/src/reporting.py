from __future__ import annotations

from pathlib import Path


def ensure_output_dirs(output_dir: str | Path) -> None:
    output_dir = Path(output_dir)
    for subdir in ["figures", "tables"]:
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)


def save_text(path: str | Path, content: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
