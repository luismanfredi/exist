from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATA_PATH = DATA_DIR / "raw" / "star_classification.csv"
output_data_dir = DATA_DIR / "processed"
