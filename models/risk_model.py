from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PatientSignals:
    heart_rate: float
    oxygen_level: float
    respiratory_rate: float
    blood_pressure: float


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(minimum, min(maximum, value))


def predict_risk(signals: PatientSignals) -> dict:
    score = 0.0
    factors: list[str] = []

    if signals.heart_rate >= 120:
        score += 0.25
        factors.append("tachycardia")
    elif signals.heart_rate >= 100:
        score += 0.14
        factors.append("elevated_heart_rate")

    if signals.oxygen_level <= 90:
        score += 0.32
        factors.append("critical_oxygen_level")
    elif signals.oxygen_level <= 94:
        score += 0.20
        factors.append("low_oxygen_level")

    if signals.respiratory_rate >= 28:
        score += 0.24
        factors.append("high_respiratory_rate")
    elif signals.respiratory_rate >= 22:
        score += 0.13
        factors.append("elevated_respiratory_rate")

    if signals.blood_pressure >= 160:
        score += 0.18
        factors.append("high_blood_pressure")
    elif signals.blood_pressure >= 140:
        score += 0.10
        factors.append("elevated_blood_pressure")

    score = round(_clamp(score), 2)

    if score >= 0.70:
        level = "high"
    elif score >= 0.35:
        level = "moderate"
    else:
        level = "low"

    return {
        "risk_score": score,
        "risk_level": level,
        "detected_factors": factors,
        "model_type": "deterministic_demo_scoring"
    }
