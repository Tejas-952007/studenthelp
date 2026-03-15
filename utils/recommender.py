from __future__ import annotations

from typing import Any

ARCHETYPES = {
    0: "The Overloaded Achiever",
    1: "The Disengaged Drifter",
    2: "The Silent Struggler",
    3: "The Social Learner",
    4: "The Digital Native",
    5: "The Resilient Balanced",
}


def generate_recommendations(scores: dict[str, Any], predictions: dict[str, Any]) -> dict[str, Any]:
    stress = scores["stress_index"]
    mode = predictions.get("learning_mode", "Hybrid")

    if stress >= 0.75:
        stress_tips = ["10-min evening walk", "4-7-8 breathing", "No-screen 30 mins before sleep"]
    elif stress >= 0.45:
        stress_tips = ["Pomodoro 25-5 cycles", "Short stretch breaks", "Weekly social activity"]
    else:
        stress_tips = ["Keep current routine", "Progress journaling", "Weekend hobby block"]

    schedule = [
        "06:30 Wake up + hydration",
        "07:00 Light movement / breathing",
        "08:00 Focus study block",
        "11:00 Break + snack",
        "14:00 Revision / assignments",
        "18:00 Outdoor / social time",
        "22:30 Wind down + sleep",
    ]

    return {
        "learning_mode": mode,
        "daily_schedule": schedule,
        "stress_tips": stress_tips,
        "book_recs": ["Atomic Habits", "Deep Work", "The Power of Now"],
        "game_recs": ["Sudoku", "Chess puzzles"],
        "edtech_recs": ["NPTEL", "SWAYAM", "YouTube playlists"],
        "roadmap_30_60_90": {
            "30": "Fix sleep + study consistency",
            "60": "Track weekly goals + mock tests",
            "90": "Capstone project / portfolio milestone",
        },
    }


def generate_student_report(answers: dict[str, Any], scores: dict[str, Any], recs: dict[str, Any]) -> str:
    return (
        f"Student: {answers.get('name', 'N/A')}\n"
        f"Recommended mode: {recs['learning_mode']}\n"
        f"Stress index: {scores['stress_index']}\n"
        f"Anxiety level: {scores['anxiety_level']}\n"
        f"Motivation score: {scores['motivation_score']}\n"
    )


def generate_parent_report(answers: dict[str, Any], scores: dict[str, Any]) -> str:
    return (
        "Your child may benefit from a calmer routine and predictable study slots. "
        f"Current stress index is {scores['stress_index']}, so focus on sleep, supportive conversation, "
        "and non-judgmental weekly check-ins."
    )
