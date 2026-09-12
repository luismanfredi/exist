from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from exist.config import RF_PARAMS


def build_model() -> Pipeline:
    return Pipeline([("model", RandomForestClassifier(**RF_PARAMS))])
