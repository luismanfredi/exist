import logging
from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI, HTTPException

from exist.api.schemas import ObjectFeatures, ObjectPrediction
from exist.config import MODEL_DIR
from exist.db.db import log_prediction
from exist.utils import complete_table

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = joblib.load(MODEL_DIR / "random_forest_v1" / "model.joblib")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict", response_model=ObjectPrediction)
def predict(features: ObjectFeatures) -> ObjectPrediction:
    model = app.state.model
    values = complete_table(features)
    try:
        pred = model.predict(values)[0]
        proba = model.predict_proba(values)[0].max()
    except Exception as e:  # noqa BLE001
        raise HTTPException(status_code=500, detail=f"prediction error: {e}")

    try:
        converted_data = {str(k): float(v) for k, v in features.model_dump().items()}
        log_prediction(converted_data, pred, proba, "Random_Forest_V1")
    except Exception:
        logger.exception("Failed to log prediction")

    return ObjectPrediction(predicted_class=str(pred), confidence=float(proba))
