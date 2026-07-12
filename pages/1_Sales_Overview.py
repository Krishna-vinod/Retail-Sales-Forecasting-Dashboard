import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Sales Overview Dashboard")

# Load dataset
df = pd.read_csv("train.csv")
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d/%m/%Y"
)
# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Filters")

selected_region = st.sidebar.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

filtered = df.copy()

if selected_region != "All":
    filtered = filtered[filtered["Region"] == selected_region]

if selected_category != "All":
    filtered = filtered[filtered["Category"] == selected_category]

# -------------------------
# KPI Cards
# -------------------------

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${filtered['Sales'].sum():,.0f}")
col2.metric("Orders", filtered.shape[0])
col3.metric("Average Order Value", f"${filtered['Sales'].mean():,.0f}")

st.divider()

# -------------------------
# Total Sales by Year
# -------------------------

st.subheader("Total Sales by Year")

yearly = (
    filtered.groupby(filtered["Order Date"].dt.year)["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(yearly.index.astype(str), yearly.values)

ax.set_xlabel("Year")
ax.set_ylabel("Sales")

st.pyplot(fig)

# -------------------------
# Monthly Sales Trend
# -------------------------

st.subheader("Monthly Sales Trend")

monthly = (
    filtered.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(11,4))

ax.plot(monthly.index, monthly.values, linewidth=2)

ax.set_xlabel("Date")
ax.set_ylabel("Sales")

st.pyplot(fig)

# -------------------------
# Region Sales
# -------------------------

st.subheader("Sales by Region")

region_sales = (
    filtered.groupby("Region")["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(7,4))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values,
    ax=ax
)

st.pyplot(fig)

# -------------------------
# Category Sales
# -------------------------

st.subheader("Sales by Category")

category_sales = (
    filtered.groupby("Category")["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(7,4))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values,
    ax=ax
)

st.pyplot(fig)
