import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="By Country", layout="wide")

st.title("🇮🇳 By Country / Operator — Sample Data")

# Sample country-level breakdown (editable)
country_data = [
    {"country":"USA","satellites":6800,"notes":"Commercial + government"},
    {"country":"China","satellites":2200,"notes":"Rapid commercial growth"},
    {"country":"India","satellites":136,"notes":"ISRO + private players"},
    {"country":"Russia","satellites":400,"notes":"Legacy + modern systems"},
    {"country":"EU/ESA","satellites":200,"notes":"Collective European assets"},
    {"country":"Other","satellites":2400,"notes":"Smallsat operators worldwide"}
]

df = pd.DataFrame(country_data)

st.dataframe(df.style.format({"satellites":"{:,}"}), height=360)

st.markdown("### How satellites help India (examples)")
st.write(
    "- *Earth observation*: Crop health, water resources, disaster response.\n"
    "- *Navigation & timing*: Regional navigation support and precise timing.\n"
    "- *Telecom*: Connectivity to remote and rural areas.\n"
    "- *Science*: Research, planetary missions, space tech development."
)

st.markdown("---")
st.write("*How to replace this table with real data*: create data/by_country.csv with columns: country, satellites, notes, then use pd.read_csv to load it.")
