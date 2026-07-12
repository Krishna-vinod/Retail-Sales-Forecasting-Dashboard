# 📊 Retail Sales Forecasting Dashboard

An interactive multi-page **Streamlit dashboard** for retail sales analysis, forecasting, anomaly detection, and product demand segmentation using Machine Learning and Data Analytics techniques.

---

## 🚀 Features

### 📈 Sales Overview
- Monthly sales trend visualization
- Sales by Category
- Sales by Region
- Interactive charts
- Business insights

### 🔮 Forecast Explorer
- Sales forecasting using **XGBoost**
- Forecast visualization for:
  - Furniture
  - Technology
  - Office Supplies
  - East Region
  - West Region
- Adjustable forecast horizon
- Model performance metrics (MAE & RMSE)

### 🚨 Anomaly Report
- Detect unusual sales values
- Interactive anomaly visualization
- Highlights abnormal sales patterns

### 📦 Product Demand Segments
- Product segmentation using **K-Means Clustering**
- PCA visualization of clusters
- Cluster statistics
- Demand segment classification
- Inventory stocking recommendations

---

# 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost

---

# 📂 Project Structure

```
Retail-Sales-Forecasting-Dashboard
│
├── app.py
├── requirements.txt
├── train.csv
├── README.md
│
└── pages
    ├── 1_Sales_Overview.py
    ├── 2_Forecast_Explorer.py
    ├── 3_Anomali_Report.py
    └── 4_Product_Demand_Segments.py
```

---

# 📊 Machine Learning Models

| Module | Algorithm |
|---------|-----------|
| Sales Forecasting | XGBoost Regressor |
| Product Segmentation | K-Means Clustering |
| Dimensionality Reduction | PCA |

---

# 📈 Dashboard Pages

## 1️⃣ Sales Overview
- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Interactive Visualizations

## 2️⃣ Forecast Explorer
- XGBoost Forecast
- Forecast Horizon Selection
- Forecast Table
- Performance Metrics

## 3️⃣ Anomaly Report
- Sales Outlier Detection
- Monthly Anomaly Visualization
- Summary Statistics

## 4️⃣ Product Demand Segments
- K-Means Product Clustering
- PCA Scatter Plot
- Cluster Statistics
- Inventory Recommendations

---

# 📦 Dataset

Dataset used:

**Superstore Sales Dataset**

Contains:

- Orders
- Products
- Categories
- Regions
- Customers
- Sales

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Krishna-vinod/Retail-Sales-Forecasting-Dashboard.git
```

Move into the project folder

```bash
cd Retail-Sales-Forecasting-Dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📷 Screenshots

Screenshots will be added after deployment.


- Sales Overview
- Forecast Explorer
- Anomaly Report
- Product Demand Segments

---

# 🌐 Live Demo

Deployment in progress.

The application will be available on Streamlit Community Cloud.
---

# 👨‍💻 Author

**Krishna Vinod**

B.Tech Artificial Intelligence & Data Science

KMCT Institute of Emerging Technology and Management

---

# 📄 License

This project is developed for educational and academic purposes.
