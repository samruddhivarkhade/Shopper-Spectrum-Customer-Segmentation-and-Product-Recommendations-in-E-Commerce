import streamlit as st
import pickle
import numpy as np

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

# ----------------------------
# Load Models
# ----------------------------
kmeans = pickle.load(open("models/kmeans.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
item_similarity = pickle.load(open("models/item_similarity.pkl", "rb"))

product_list = sorted(item_similarity.columns.tolist())

# ----------------------------
# Helper Functions
# ----------------------------
def predict_segment(recency, frequency, monetary):
    data = np.array([[recency, frequency, monetary]])
    data_scaled = scaler.transform(data)
    cluster = kmeans.predict(data_scaled)[0]

    segment_map = {
        0: ("High-Value", "💎"),
        1: ("Regular", "🙂"),
        2: ("Occasional", "🛍️"),
        3: ("At-Risk", "⚠️")
    }

    return segment_map.get(cluster, ("Unknown", "❓"))


def recommend_products(product_name, top_n=5):
    return (
        item_similarity[product_name]
        .sort_values(ascending=False)
        .iloc[1:top_n+1]
        .index
        .tolist()
    )

# ----------------------------
# Header
# ----------------------------
st.title("🛒 Shopper Spectrum")
st.markdown("### Customer Segmentation & Personalized Recommendations")
st.markdown("---")

# ----------------------------
# Tabs
# ----------------------------
tab1, tab2 = st.tabs([
    "🎯 Product Recommendation",
    "👥 Customer Segmentation"
])

# ----------------------------
# TAB 1: Product Recommendation
# ----------------------------
with tab1:
    st.markdown("#### 🔍 Recommend Similar Products")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    product_name = st.selectbox(
        "Select a Product",
        product_list
    )

    if st.button("✨ Get Recommendations"):
        recommendations = recommend_products(product_name)

        st.success("Top 5 Similar Products")
        for prod in recommendations:
            st.markdown(f"🟣 **{prod}**")

    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# TAB 2: Customer Segmentation
# ----------------------------
with tab2:
    st.markdown("#### 📊 Predict Customer Segment")

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input("📅 Recency (days)", min_value=0)

    with col2:
        frequency = st.number_input("🔁 Frequency", min_value=0)

    with col3:
        monetary = st.number_input("💰 Monetary", min_value=0.0)

    if st.button("🚀 Predict Segment"):
        segment, icon = predict_segment(recency, frequency, monetary)

        st.markdown(
            f"""
            <div class="card">
                <h3>{icon} {segment} Customer</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("Samruddhi Varkhade @2026 | Shopper Spectrum")
