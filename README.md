# Shopper-Spectrum-Customer-Segmentation-and-Product-Recommendations-in-E-Commerce

# Shopper Spectrum  
### Customer Segmentation & Product Recommendation System

Shopper Spectrum is a machine learning-based e-commerce analytics project that analyzes customer purchase behavior to perform **customer segmentation** and **personalized product recommendations**. The project uses **RFM analysis**, **KMeans clustering**, and **collaborative filtering**, and is deployed as an interactive **Streamlit web application**.

---

## Problem Statement
E-commerce platforms generate large volumes of transactional data daily. Analyzing this data helps businesses understand customer behavior, segment customers effectively, and recommend relevant products to improve user experience and business growth.

This project aims to:
- Segment customers based on purchasing behavior
- Identify high-value and at-risk customers
- Recommend similar products using purchase history

---

## Machine Learning Approach

### 1️. Customer Segmentation
- **RFM Analysis**
  - Recency: Days since last purchase
  - Frequency: Number of transactions
  - Monetary: Total spending
- **Algorithm:** KMeans Clustering
- **Customer Segments:**
  -  High-Value
  -  Regular
  -  Occasional
  -  At-Risk

### 2️. Product Recommendation
- **Technique:** Item-based Collaborative Filtering
- **Similarity Metric:** Cosine Similarity
- Recommends top 5 similar products based on purchase patterns

---

## Features
- Cleaned and preprocessed real-world retail dataset
- Automated RFM feature engineering
- Business-oriented customer segmentation
- Real-time product recommendation
- Interactive Streamlit UI
- Light & Dark mode support
- Dropdown-based product selection

---

## Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Matplotlib, Seaborn**
- **Streamlit**
- **Pickle**

---
## How to Run the Project

### 1. Install Dependencies
pip install -r requirements.txt

### 2️. Train Models
python train.py

### 3️. Run Streamlit App
streamlit run app.py
