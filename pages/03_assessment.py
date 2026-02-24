import streamlit as st

from utils.preprocessor import compute_psychological_scores, encode_input, get_student_archetype
from utils.recommender import ARCHETYPES

st.title("📝 Find Your Perfect Learning Style – Quick Check-In")
st.caption("This is not a clinical test. Results are for self-reflection only.")

with st.form("assessment_form"):
    name = st.text_input("Name")
    study_hours = st.slider("Study hours/day", 0, 12, 4)
    class_hours = st.number_input("Class hours/week", 0, 60, 24)
    confidence = st.slider("When explaining a topic to a friend, comfort level", 1, 5, 3)
    overload = st.slider("When many tasks come at once, how do you feel?", 1, 5, 3)
    sleep_hours = st.slider("Sleep hours/night", 2, 12, 7)
    social_freq = st.slider("How often do you meet friends/family?", 1, 5, 3)
    phone_hours = st.slider("Phone hours/day (outside studies)", 0, 12, 4)
    financial_stress = st.slider("Financial comfort level", 1, 5, 3)

    submitted = st.form_submit_button("Submit Assessment")

if submitted:
    answers = {
        "name": name,
        "study_hours": study_hours,
        "class_hours": class_hours,
        "confidence": confidence,
        "overload": overload,
        "sleep_hours": sleep_hours,
        "social_freq": social_freq,
        "phone_hours": phone_hours,
        "financial_stress": financial_stress,
    }

    scores = compute_psychological_scores(answers)
    vector = encode_input(answers)
    archetype_id = get_student_archetype(vector)

    if scores["digital_comfort"] >= 7 and scores["social_isolation"] <= 5:
        mode = "Online"
    elif scores["social_isolation"] >= 6:
        mode = "Offline"
    else:
        mode = "Hybrid"

    st.session_state.answers = answers
    st.session_state.scores = scores
    st.session_state.predictions = {
        "learning_mode": mode,
        "archetype": ARCHETYPES[archetype_id],
    }
    st.session_state.assessment_submitted = True

    st.success("Assessment submitted! Visit Page 4 for your AI results.")
