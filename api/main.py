from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from models.risk_model import PatientSignals, predict_risk


app = FastAPI(
    title="MedPredictRT",
    description="Prototype API for real-time medical risk scoring using simulated patient signals.",
    version="0.1.0",
)


class PredictionRequest(BaseModel):
    patient_id: str = Field(default="demo-patient")
    heart_rate: float = Field(..., ge=20, le=240)
    oxygen_level: float = Field(..., ge=50, le=100)
    respiratory_rate: float = Field(..., ge=5, le=80)
    blood_pressure: float = Field(..., ge=60, le=260)


@app.get("/")
def health_check() -> dict:
    return {
        "service": "MedPredictRT",
        "status": "running",
        "mode": "prototype",
    }


@app.post("/predict")
def predict(payload: PredictionRequest) -> dict:
    signals = PatientSignals(
        heart_rate=payload.heart_rate,
        oxygen_level=payload.oxygen_level,
        respiratory_rate=payload.respiratory_rate,
        blood_pressure=payload.blood_pressure,
    )

    result = predict_risk(signals)

    return {
        "patient_id": payload.patient_id,
        **result,
    }
