from contextlib import asynccontextmanager

import joblib
from fastapi import FastAPI, HTTPException

from exist.api.schemas import ObjectFeatures, ObjectPrediction
from exist.config import MODEL_DIR
from exist.utils import complete_table


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

    return ObjectPrediction(predicted_class=str(pred), confidence=float(proba))
