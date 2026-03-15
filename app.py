import streamlit as st

st.set_page_config(
    page_title="Student Psychological Health Analyzer",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 Comparative Analysis: Online vs Offline Learning")
st.caption("Pune, Maharashtra focused AI-assisted student wellbeing insight platform")

st.markdown(
    """
Welcome! Use the sidebar to navigate through the 7-page experience:

1. Information Hub
2. Global Context
3. Assessment
4. Results Dashboard
5. Full Report
6. Parent View
7. Teacher View

> ⚠️ Disclaimer: This tool is not a clinical diagnosis system. It supports self-reflection and guidance.
"""
)

st.info("Start from **Page 1: Information Hub** and proceed in order for the best experience.")

if "assessment_submitted" not in st.session_state:
    st.session_state.assessment_submitted = False
