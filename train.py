# train.py

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.rfm import create_rfm
from src.clustering import train_kmeans
from src.recommender import train_recommender
import pickle
import pandas as pd

# Load & clean
df = load_data("data/OnlineRetail.csv")
df = clean_data(df)

# RFM
rfm = create_rfm(df)

# Clustering
rfm, kmeans, scaler = train_kmeans(rfm)

# Recommender
item_similarity = train_recommender(df)

# Save models
pickle.dump(kmeans, open("models/kmeans.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(item_similarity, open("models/item_similarity.pkl", "wb"))

print("✅ Training completed successfully")

from src.eda import plot_rfm_distribution
plot_rfm_distribution(rfm)
