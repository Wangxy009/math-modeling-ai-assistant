from __future__ import annotations

from pathlib import Path

from src.data_io import load_table, save_table
from src.eda import describe_dataframe, plot_missing_values
from src.evaluate import save_metrics
from src.modeling import run_baseline_model
from src.reporting import ensure_output_dirs, save_text


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "02_data"
OUTPUT_DIR = ROOT / "04_outputs"


def main() -> None:
    ensure_output_dirs(OUTPUT_DIR)

    data_path = DATA_DIR / "sample_input.csv"
    if not data_path.exists():
        message = (
            "No sample_input.csv found. Put your data in 02_data/ or update "
            "data_path in 03_code/main.py."
        )
        save_text(OUTPUT_DIR / "run_notes.txt", message)
        print(message)
        return

    df = load_table(data_path)
    summary = describe_dataframe(df)
    save_text(OUTPUT_DIR / "data_summary.md", summary)
    plot_missing_values(df, OUTPUT_DIR / "figures" / "missing_values.png")

    result = run_baseline_model(df)
    save_table(result.predictions, OUTPUT_DIR / "tables" / "baseline_predictions.csv")
    save_metrics(result.metrics, OUTPUT_DIR / "tables" / "baseline_metrics.csv")

    print("Experiment finished. Check 04_outputs/.")


if __name__ == "__main__":
    main()
