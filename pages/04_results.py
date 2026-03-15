import streamlit as st

from utils.recommender import generate_recommendations

st.title("📊 AI Results Dashboard")

if not st.session_state.get("assessment_submitted", False):
    st.warning("Please complete Page 3 assessment first.")
    st.stop()

answers = st.session_state.get("answers", {})
scores = st.session_state.get("scores", {})
predictions = st.session_state.get("predictions", {})
recs = generate_recommendations(scores, predictions)
st.session_state.recommendations = recs

st.metric("Recommended Learning Mode", predictions.get("learning_mode", "Hybrid"))
st.metric("Stress Index", scores.get("stress_index", 0.0))
st.metric("Anxiety Level", scores.get("anxiety_level", 0))

st.subheader("Detected archetype")
st.info(predictions.get("archetype", "The Resilient Balanced"))

st.subheader("Daily routine")
for item in recs["daily_schedule"]:
    st.write(f"- {item}")

st.subheader("Stress relief suggestions")
st.write(", ".join(recs["stress_tips"]))
