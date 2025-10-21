import streamlit as st

st.set_page_config(page_title="Global Satellites Dashboard", layout="wide")

st.title("Global Satellites Dashboard")
st.markdown(
    "Welcome — use the left sidebar (or the top pages menu) to navigate through the dashboard.\n\n"
    "This project uses the Streamlit pages/ structure. If you see separate pages on the left, click them.\n\n"
    "Pages included:\n- Overview\n- By Country\n- History & Development\n- Functionality & Uses\n- Forecasting\n"
)

st.info("Tip: If you don't see the pages in your Streamlit UI, run streamlit run app.py and open the browser link shown by Streamlit.")

st.markdown("---")
st.markdown("*Quick start*: Run streamlit run app.py in the project root.")
