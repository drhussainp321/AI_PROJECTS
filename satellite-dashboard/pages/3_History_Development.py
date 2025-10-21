import streamlit as st

st.set_page_config(page_title="History & Development", layout="wide")

st.title("📜 Inception & Development — Satellite Timeline")

st.markdown("""
*High-level timeline*

- *1957* — Sputnik 1: first artificial satellite (start of space age).
- *1960s–1980s* — Development of communications, weather, and scientific satellites.
- *1990s* — Miniaturization, growth of commercial communications satellites.
- *2000s* — Expansion of Earth observation and GNSS modernization.
- *2010s–2020s* — Rise of CubeSats, smallsats, and mega-constellations.

*Development stages (engineering view)*

1. Mission concept & requirements
2. Platform & payload design (bus, power, ADCS, comms)
3. Integration & testing (vibration, thermal, EMI/EMC)
4. Launch & early orbit operations (LEOP)
5. Routine operations, data processing, EOL planning
""")

st.markdown("---")
st.subheader("Key engineering subsystems")
st.write(
    "- *Power*: solar arrays, batteries, power regulation.\n"
    "- *Attitude*: reaction wheels, magnetorquers, star trackers.\n"
    "- *Communications*: radios, antennas, modems.\n"
    "- *Payload*: sensors, imagers, transponders."
)
