from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATA_PATH = DATA_DIR / "raw" / "star_classification.csv"
output_data_dir = DATA_DIR / "processed" / "processed_star_classification.parquet"

RF_PARAMS = {
    "n_estimators": 300,
    "max_depth": 20,
    "min_samples_leaf": 1,
    "max_features": "log2",
}

MODEL_DIR = Path(__file__).resolve().parents[2] / "models"
