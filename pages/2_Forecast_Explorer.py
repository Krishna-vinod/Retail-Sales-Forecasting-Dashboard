import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

st.title("🔮 Forecast Explorer")

st.write("Explore the next 3 months sales forecast using the best forecasting model (XGBoost).")

forecast_data = pd.DataFrame({
    "Date": pd.to_datetime([
        "2019-01-31",
        "2019-02-28",
        "2019-03-31"
    ]),
    "Furniture": [31425.17, 9716.00, 6214.69],
    "Technology": [21819.18, 20182.09, 24370.32],
    "Office Supplies": [29633.47, 25796.03, 25957.26],
    "West": [29677.77, 11175.51, 15125.34],
    "East": [19581.69, 25088.46, 25353.45]
})


option = st.selectbox(
    "Select Category / Region",
    [
        "Furniture",
        "Technology",
        "Office Supplies",
        "West",
        "East"
    ]
)

months = st.slider(
    "Forecast Horizon (Months)",
    min_value=1,
    max_value=3,
    value=3
)

forecast = forecast_data.iloc[:months]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    forecast["Date"],
    forecast[option],
    marker="o",
    linewidth=3,
    markersize=8
)

ax.set_title(f"{option} Monthly Sales Forecast", fontsize=16)
ax.set_xlabel("Forecast Month")
ax.set_ylabel("Forecast Sales ($)")

ax.set_xticks(forecast["Date"])
ax.set_xticklabels(
    forecast["Date"].dt.strftime("%b %Y"),
    rotation=45
)
plt.xticks(rotation=45)

ax.grid(True, linestyle="--", alpha=0.5)

fig.tight_layout()

st.pyplot(fig)

st.subheader("📋 Forecast Values")

table = forecast.copy()
table["Date"] = table["Date"].dt.strftime("%b %Y")
table[option] = table[option].map(lambda x: f"${x:,.2f}")

st.dataframe(
    table[["Date", option]],
    use_container_width=True
)

st.subheader("📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Best Model",
        value="XGBoost"
    )

with col2:
    st.metric(
        label="MAE",
        value="13,915.32"
    )

with col3:
    st.metric(
        label="RMSE",
        value="18,893.85"
    )

st.info(
    """
**Interpretation**

- The graph shows the predicted sales for the selected category or region.
- Forecast values are generated using the **XGBoost** forecasting model.
- Lower MAE and RMSE indicate better prediction accuracy.
"""
)
