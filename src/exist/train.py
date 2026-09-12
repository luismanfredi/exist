import json
import sys
from datetime import UTC, datetime

import joblib
import pandas as pd
import sklearn
from pyprojroot import here
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from src.exist.config import MODEL_DIR, RF_PARAMS, output_data_dir
from src.exist.model import build_model

sys.path.append(str(here()))


def main() -> None:
    df = pd.read_parquet(output_data_dir)
    X = df.drop("class", axis=1).values
    y = df["class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_model()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average="macro")
    print(f"F1 macro (test): {f1:.3f}")

    joblib.dump(model, MODEL_DIR / "random_forest_v1" / "model.joblib")
    metadata = {
        "hyperparameters": RF_PARAMS,
        "test_f1_macro": f1,
        "sklearn_version": sklearn.__version__,
        "trained_at": datetime.now(tz=UTC).isoformat(),
    }
    (MODEL_DIR / "random_forest_v1" / "metadata.json").write_text(
        json.dumps(metadata, indent=2)
    )


if __name__ == "__main__":
    main()
