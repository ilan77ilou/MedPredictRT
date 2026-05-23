from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(
    title="MedPredictRT API",
    description="Real-time medical prediction API",
    version="0.1"
)

class PatientData(BaseModel):
    heart_rate: float
    oxygen_level: float
    respiratory_rate: float
    blood_pressure: float

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/predict")
def predict(data: PatientData):

    risk_score = round(random.uniform(0.1, 0.99), 2)

    if risk_score > 0.8:
        prediction = "High risk"
    elif risk_score > 0.5:
        prediction = "Moderate risk"
    else:
        prediction = "Low risk"

    return {
        "risk_score": risk_score,
        "prediction": prediction
    }