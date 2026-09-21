from pydantic import BaseModel


class ObjectFeatures(BaseModel):
    u: float
    g: float
    r: float
    i: float
    z: float
    redshift: float


class ObjectPrediction(BaseModel):
    predicted_class: str
    confidence: float
