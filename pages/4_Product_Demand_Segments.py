import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.title("📦 Product Demand Segments")
st.write("Product demand segmentation using K-Means Clustering.")

df = pd.read_csv("train.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

monthly = (
    df.groupby(
        ["Sub-Category", pd.Grouper(key="Order Date", freq="ME")]
    )["Sales"]
    .sum()
    .reset_index()
)

segment = monthly.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Order_Value=("Sales", "mean"),
    Sales_Volatility=("Sales", "std")
).reset_index()

segment["Sales_Volatility"] = segment["Sales_Volatility"].fillna(0)

features = [
    "Total_Sales",
    "Avg_Order_Value",
    "Sales_Volatility"
]

X = segment[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

segment["Cluster"] = kmeans.fit_predict(X_scaled)

cluster_summary = (
    segment.groupby("Cluster")[features]
    .mean()
    .sort_values("Total_Sales")
)

cluster_order = cluster_summary.index.tolist()

cluster_names = {
    cluster_order[0]: "Low Volume • Stable Demand",
    cluster_order[1]: "Moderate Demand",
    cluster_order[2]: "Growing Demand",
    cluster_order[3]: "High Volume • Stable Demand"
}

segment["Cluster Name"] = segment["Cluster"].map(cluster_names)

cluster_summary["Cluster Name"] = (
    cluster_summary.index.map(cluster_names)
)

cluster_summary = cluster_summary[
    [
        "Cluster Name",
        "Total_Sales",
        "Avg_Order_Value",
        "Sales_Volatility",
    ]
]

st.subheader("📊 Cluster Statistics")
cluster_summary = cluster_summary.round(2)

pca = PCA(n_components=2)

points = pca.fit_transform(X_scaled)

segment["PC1"] = points[:, 0]
segment["PC2"] = points[:, 1]

fig, ax = plt.subplots(figsize=(10, 6))

for cluster in sorted(segment["Cluster"].unique()):

    data = segment[segment["Cluster"] == cluster]

    ax.scatter(
        data["PC1"],
        data["PC2"],
        s=80,
        label=cluster_names[cluster]
    )

    for _, row in data.iterrows():

        ax.text(
            row["PC1"],
            row["PC2"],
            row["Sub-Category"],
            fontsize=8
        )

ax.set_title("Product Demand Segmentation")
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.legend()

st.pyplot(fig)
st.info(
    """
    **Interpretation**

    • Products close together have similar demand patterns.

    • Different colors represent different demand segments identified using K-Means.

    • Businesses can use these segments for inventory planning and demand forecasting.
    """
)

st.subheader("📋 Demand Segments")

display_df = segment[
    [
        "Sub-Category",
        "Cluster Name",
        "Total_Sales",
        "Avg_Order_Value",
        "Sales_Volatility"
    ]
].sort_values(
    by=["Cluster Name", "Total_Sales"],
    ascending=[True, False]
)
display_df["Total_Sales"] = display_df["Total_Sales"].round(2)
display_df["Avg_Order_Value"] = display_df["Avg_Order_Value"].round(2)
display_df["Sales_Volatility"] = display_df["Sales_Volatility"].round(2)
st.dataframe(display_df, use_container_width=True)
st.subheader("📦 Recommended Stocking Strategy")

strategy = pd.DataFrame({
    "Demand Segment": [
        "High Volume • Stable Demand",
        "Growing Demand",
        "Moderate Demand",
        "Low Volume • Stable Demand"
    ],
    "Recommended Strategy": [
        "Maintain high inventory levels and replenish frequently to avoid stock-outs.",
        "Gradually increase inventory while closely monitoring demand trends.",
        "Maintain balanced inventory and review stock levels monthly.",
        "Keep minimum inventory and restock only when required."
    ]
})

st.table(strategy)
