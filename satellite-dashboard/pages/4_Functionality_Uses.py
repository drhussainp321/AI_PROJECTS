import streamlit as st

st.set_page_config(page_title="Functionality & Uses", layout="wide")

st.title("🔧 Functionality & Societal Uses of Satellites")

st.markdown("### Global benefits")
st.write(
    "- *Telecommunications*: broadband, broadcast, and remote comms.\n"
    "- *Earth Observation*: agriculture monitoring, disaster response.\n"
    "- *Navigation*: GNSS services for positioning & timing.\n"
    "- *Science*: space weather, astronomy, planetary exploration.\n"
    "- *Security & Maritime*: ship tracking and surveillance (subject to export/regulation)."
)

st.markdown("### Focused examples for India")
st.write(
    "- Agriculture: NDVI, crop forecasting, precision farming.\n"
    "- Disaster management: flood/cyclone monitoring, early warnings.\n"
    "- Urban planning: high-resolution mapping, land-use monitoring.\n"
    "- Connectivity: bridging digital divide using satellite internet."
)

st.markdown("---")
st.info("You can extend this page to include case studies: link satellite product examples (imagery, derived indices) and sample workflows for Indian agencies.")

