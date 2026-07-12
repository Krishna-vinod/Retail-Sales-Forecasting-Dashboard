import streamlit as st

st.set_page_config(
    page_title="Retail Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Forecasting Dashboard")

st.markdown("""
Welcome to the Retail Sales Forecasting Dashboard.

Use the sidebar to navigate between:

- 📈 Sales Overview
- 🔮 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments
""")