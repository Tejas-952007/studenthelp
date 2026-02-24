import streamlit as st

from utils.recommender import generate_student_report
from utils.report_generator import build_pdf_report

st.title("📄 Full Psychological Report")

if not st.session_state.get("assessment_submitted", False):
    st.warning("Please complete Page 3 assessment first.")
    st.stop()

answers = st.session_state.get("answers", {})
scores = st.session_state.get("scores", {})
recs = st.session_state.get("recommendations", {})

report = generate_student_report(answers, scores, recs)
st.text_area("Report Preview", report, height=220)

if st.button("Generate PDF"):
    path = build_pdf_report("Student Psychological Health Report", report, "student_report.pdf")
    with open(path, "rb") as f:
        st.download_button("Download Report", f, file_name="student_report.pdf")
