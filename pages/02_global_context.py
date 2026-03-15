import pandas as pd
import plotly.express as px
import streamlit as st

st.title("🌍 Global Context & Hybrid Learning")

adoption_df = pd.DataFrame(
    {
        "country": ["India", "USA", "UK", "Germany", "Australia"],
        "adoption": [62, 74, 70, 58, 66],
    }
)

fig = px.bar(adoption_df, x="country", y="adoption", title="Online Learning Adoption (%)")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Hybrid learning")
st.info("Synthetic insight: 67% of Pune engineering students prefer hybrid post-COVID.")
