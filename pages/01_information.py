import streamlit as st

st.title("📘 Information Hub: Online vs Offline Learning")
st.markdown("### Marathi + English intro")
st.write("**मराठी:** योग्य learning method तुमच्या मनाला suit झाला पाहिजे, trend ला नाही.")
st.write("**English:** The best learning method is the one that fits your mind, not the trend.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Online Learning")
    st.success("Pros: Flexibility, self-paced, broad content access")
    st.warning("Cons: Screen fatigue, distraction risk, isolation")

with col2:
    st.subheader("Offline Learning")
    st.success("Pros: Social engagement, structure, real-time mentorship")
    st.warning("Cons: Commute time, fixed schedule, pace mismatch")

if st.button("Find My Learning Style →"):
    st.switch_page("pages/03_assessment.py")
