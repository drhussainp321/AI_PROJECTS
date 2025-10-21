import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

st.set_page_config(page_title="Forecasting", layout="wide")

st.title("📈 Forecasting Active Satellites — Demo")

DATA_PATH = Path(__file__).parents[1] / "data" / "sample_counts.csv"
try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error(f"Could not load sample CSV: {e}")
    df = pd.DataFrame({"year":[], "active_satellites":[]})

if df.empty:
    st.write("No historical data to run forecasting.")
else:
    years = df['year'].values.reshape(-1, 1)
    counts = df['active_satellites'].values

    # Fit simple linear regression (demo)
    model = LinearRegression()
    model.fit(years, counts)

    future_years = np.arange(df['year'].max()+1, df['year'].max()+6)
    future_years_reshaped = future_years.reshape(-1,1)
    preds = model.predict(future_years_reshaped).astype(int)

    df_future = pd.DataFrame({
        'year': future_years,
        'predicted_active_satellites': preds
    })

    st.subheader("Historical data")
    st.dataframe(df.set_index('year'))

    st.subheader("Forecast (linear regression - demo)")
    st.dataframe(df_future.set_index('year'))

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['year'], y=df['active_satellites'], mode='lines+markers', name='historical'))
    fig.add_trace(go.Scatter(x=df_future['year'], y=df_future['predicted_active_satellites'], mode='lines+markers', name='predicted'))
    fig.update_layout(title='Historical + Forecast (demo)', xaxis_title='Year', yaxis_title='Active satellites')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("*Limitations:* This linear model is a simple demonstration. Real forecasting must incorporate launch manifests, constellation plans, deorbit policies, and scenario analysis.")

    st.markdown("---")
    st.write("*How to improve:* Use time series models (Prophet, ARIMA), incorporate operator manifests, include deorbit schedules, and build scenario-based forecasts.")
