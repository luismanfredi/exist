from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from src.exist.config import RF_PARAMS


def build_model() -> Pipeline:
    return Pipeline([("model", RandomForestClassifier(**RF_PARAMS))])
