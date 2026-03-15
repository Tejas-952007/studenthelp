import streamlit as st

from utils.recommender import generate_parent_report

st.title("👨‍👩‍👧 Parent View")

if not st.session_state.get("assessment_submitted", False):
    st.warning("Please complete Page 3 assessment first.")
    st.stop()

report = generate_parent_report(
    st.session_state.get("answers", {}),
    st.session_state.get("scores", {}),
)

st.write(report)
st.subheader("What to say")
st.write("- I am with you, we can plan this together.")
st.write("- Let us build a weekly routine without pressure.")

st.subheader("What NOT to say")
st.write("- Why are you always behind?")
st.write("- Others are doing better than you.")
