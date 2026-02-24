import pandas as pd
import plotly.express as px
import streamlit as st

st.title("🏫 Teacher / Faculty Policy Insights")

dist = pd.DataFrame(
    {
        "stress_level": ["Low", "Medium", "High", "Critical"],
        "count": [22, 41, 26, 11],
    }
)

mode = pd.DataFrame(
    {
        "mode": ["Online", "Offline", "Hybrid"],
        "count": [34, 29, 37],
    }
)

st.plotly_chart(px.bar(dist, x="stress_level", y="count", title="Class Stress Distribution"), use_container_width=True)
st.plotly_chart(px.pie(mode, names="mode", values="count", title="Learning Mode Preference"), use_container_width=True)

st.info("At-risk students (anonymized count): 11")
st.write("Recommendations: blend active learning, reduce deadline clustering, and run weekly mentor check-ins.")
