from typing import Any

import joblib
import numpy as np
from numpy.typing import NDArray
from sklearn.pipeline import Pipeline

from exist.config import MODEL_DIR


def load_model() -> Pipeline:
    return joblib.load(MODEL_DIR / "model.joblib")


def predict(
    model: Pipeline, X: np.ndarray
) -> NDArray[Any] | tuple[NDArray[Any], NDArray[Any]]:
    return model.predict(X)
