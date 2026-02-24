from __future__ import annotations

from typing import Any

import numpy as np


def _scale(value: float, min_v: float, max_v: float) -> float:
    if max_v == min_v:
        return 0.0
    clipped = max(min_v, min(max_v, value))
    return (clipped - min_v) / (max_v - min_v)


def compute_psychological_scores(raw_answers: dict[str, Any]) -> dict[str, float | int]:
    sleep_hours = float(raw_answers.get("sleep_hours", 7))
    study_hours = float(raw_answers.get("study_hours", 3))
    phone_hours = float(raw_answers.get("phone_hours", 3))
    confidence = float(raw_answers.get("confidence", 3))
    overload = float(raw_answers.get("overload", 3))
    social_freq = float(raw_answers.get("social_freq", 3))
    financial_stress = float(raw_answers.get("financial_stress", 3))

    stress_index = (
        0.30 * _scale(overload, 1, 5)
        + 0.20 * (1 - _scale(sleep_hours, 2, 12))
        + 0.20 * _scale(phone_hours, 0, 12)
        + 0.15 * _scale(financial_stress, 1, 5)
        + 0.15 * (1 - _scale(social_freq, 1, 5))
    )

    anxiety_level = int(
        100
        * (
            0.5 * _scale(overload, 1, 5)
            + 0.3 * (1 - _scale(confidence, 1, 5))
            + 0.2 * (1 - _scale(sleep_hours, 2, 12))
        )
    )

    motivation_score = int(
        100
        * (
            0.35 * _scale(study_hours, 0, 12)
            + 0.35 * _scale(confidence, 1, 5)
            + 0.30 * (1 - _scale(phone_hours, 0, 12))
        )
    )

    social_isolation = round(10 * (1 - _scale(social_freq, 1, 5)), 2)
    digital_comfort = round(10 * _scale(phone_hours, 0, 12), 2)
    academic_risk_flag = int(stress_index > 0.62 and motivation_score < 45)

    return {
        "stress_index": round(stress_index, 3),
        "anxiety_level": anxiety_level,
        "motivation_score": motivation_score,
        "social_isolation": social_isolation,
        "digital_comfort": digital_comfort,
        "academic_risk_flag": academic_risk_flag,
    }


def encode_input(raw_answers: dict[str, Any]) -> np.ndarray:
    numeric_keys = [
        "study_hours",
        "class_hours",
        "confidence",
        "overload",
        "sleep_hours",
        "social_freq",
        "phone_hours",
        "financial_stress",
    ]
    vector = [float(raw_answers.get(k, 0.0)) for k in numeric_keys]
    return np.array(vector, dtype=float).reshape(1, -1)


def get_student_archetype(feature_vector: np.ndarray) -> int:
    study_hours, _, confidence, overload, sleep_hours, social_freq, phone_hours, _ = feature_vector[0]

    if overload >= 4 and study_hours >= 6:
        return 0
    if study_hours <= 2 and phone_hours >= 7:
        return 1
    if confidence <= 2 and overload >= 3:
        return 2
    if social_freq >= 4 and confidence >= 3:
        return 3
    if phone_hours >= 6 and sleep_hours >= 6:
        return 4
    return 5
