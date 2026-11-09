from __future__ import annotations

from pathlib import Path

import pandas as pd


def save_metrics(metrics: dict[str, float], path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(
        [{"metric": key, "value": value} for key, value in metrics.items()]
    )
    df.to_csv(path, index=False)


def compare_rankings(
    baseline: pd.Series, candidate: pd.Series, top_k: int = 10
) -> dict[str, float]:
    base_top = set(baseline.sort_values(ascending=False).head(top_k).index)
    cand_top = set(candidate.sort_values(ascending=False).head(top_k).index)
    overlap = len(base_top & cand_top)
    return {
        "top_k": float(top_k),
        "top_k_overlap": float(overlap),
        "top_k_overlap_rate": overlap / top_k if top_k else 0.0,
    }
