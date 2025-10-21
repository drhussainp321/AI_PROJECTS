import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Overview", layout="wide")

st.title("🌐 Overview — Global Satellites")

# Load data
DATA_PATH = Path(__file__).parents[1] / "data" / "sample_counts.csv"
try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error(f"Could not load sample CSV: {e}")
    df = pd.DataFrame({"year":[], "active_satellites":[]})

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("### Historical active satellites (sample data)")
    if not df.empty:
        fig = px.line(df, x="year", y="active_satellites", markers=True, title="Active Satellites by Year")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No historical data available.")

with col2:
    st.metric("Estimated active satellites (sample)", "14,904")
    st.write("Tracked objects (example): ~40,000")
    st.write("Major drivers: LEO constellations, smallsat growth, national programs.")

st.markdown("---")
st.markdown("*Notes:*\n- Data shown here is sample data. Replace data/sample_counts.csv with authoritative CSV or API output for live numbers.\n- Forecasting page contains a simple demo model; prefer domain models for production.")
