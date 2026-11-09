from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/math_modeling_matplotlib")

import matplotlib.pyplot as plt
import pandas as pd


def describe_dataframe(df: pd.DataFrame) -> str:
    lines = [
        "# Data Summary",
        "",
        f"- Rows: {len(df)}",
        f"- Columns: {df.shape[1]}",
        "",
        "## Columns",
        "",
    ]

    for col in df.columns:
        null_rate = df[col].isna().mean()
        dtype = df[col].dtype
        lines.append(f"- `{col}`: {dtype}, missing {null_rate:.2%}")

    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        lines.extend(
            ["", "## Numeric Description", "", "```text", numeric.describe().to_string(), "```"]
        )

    return "\n".join(lines)


def plot_missing_values(df: pd.DataFrame, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    missing_rate = df.isna().mean().sort_values(ascending=False)
    if missing_rate.empty:
        return

    plt.figure(figsize=(10, 5))
    plt.bar(missing_rate.index.astype(str), missing_rate.values, color="#2A9D8F")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Missing rate")
    plt.xlabel("Column")
    plt.title("Missing Values by Column")
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
