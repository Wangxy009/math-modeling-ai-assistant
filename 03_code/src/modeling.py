from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class ModelResult:
    predictions: pd.DataFrame
    metrics: dict[str, float]


def run_baseline_model(df: pd.DataFrame) -> ModelResult:
    """A placeholder baseline that should be replaced for each problem."""
    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        predictions = pd.DataFrame({"row_id": range(len(df)), "baseline_score": np.nan})
        return ModelResult(predictions=predictions, metrics={"n_rows": float(len(df))})

    score = numeric.fillna(numeric.median()).mean(axis=1)
    predictions = pd.DataFrame({"row_id": range(len(df)), "baseline_score": score})
    metrics = {
        "n_rows": float(len(df)),
        "n_numeric_features": float(numeric.shape[1]),
        "score_mean": float(score.mean()),
        "score_std": float(score.std(ddof=0)),
    }
    return ModelResult(predictions=predictions, metrics=metrics)


def normalize_positive(series: pd.Series) -> pd.Series:
    min_value = series.min()
    max_value = series.max()
    if max_value == min_value:
        return pd.Series(np.zeros(len(series)), index=series.index)
    return (series - min_value) / (max_value - min_value)


def normalize_negative(series: pd.Series) -> pd.Series:
    return 1 - normalize_positive(series)
