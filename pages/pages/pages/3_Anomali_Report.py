import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚨 Anomaly Report")

st.write("Sales anomalies detected using Isolation Forest and Z-Score.")

df = pd.read_csv("train.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

df = df.sort_values("Order Date")

weekly = df.groupby(
    pd.Grouper(key="Order Date", freq="W")
)["Sales"].sum().reset_index()

weekly.columns = ["Date", "Sales"]

from sklearn.ensemble import IsolationForest

iso = IsolationForest(
    contamination=0.05,
    random_state=42
)

weekly["Isolation"] = iso.fit_predict(weekly[["Sales"]])

weekly["Isolation"] = weekly["Isolation"].map({
    1:"Normal",
    -1:"Anomaly"
})

rolling_mean = weekly["Sales"].rolling(8).mean()
rolling_std = weekly["Sales"].rolling(8).std()

z = (weekly["Sales"]-rolling_mean)/rolling_std

weekly["ZScore"] = z

weekly["Z_Anomaly"] = abs(z)>2

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(
    weekly["Date"],
    weekly["Sales"],
    label="Sales"
)

anomaly = weekly[
    weekly["Isolation"]=="Anomaly"
]

ax.scatter(
    anomaly["Date"],
    anomaly["Sales"],
    color="red",
    s=60,
    label="Isolation Forest"
)

ax.legend()

st.pyplot(fig)

st.subheader("Detected Anomalies")

table = weekly[
    (weekly["Isolation"]=="Anomaly") |
    (weekly["Z_Anomaly"])
]

st.dataframe(table)

st.subheader("Observations")

st.markdown("""
- Most anomaly spikes occur during festive or promotional sales periods.
- Sudden drops may indicate supply shortages or seasonal demand changes.
- Isolation Forest detects both global and local anomalies.
- Z-Score mainly detects extreme deviations from recent sales trends.
- Several anomalies are detected by both methods, increasing confidence in those observations.
""")
