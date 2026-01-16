# src/clustering.py

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

def train_kmeans(rfm, n_clusters=4):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    # Cluster profiling
    profile = rfm.groupby('Cluster').mean()

    # Sort clusters by Monetary value
    profile = profile.sort_values('Monetary', ascending=False)

    segment_map = {}
    labels = ["High-Value", "Regular", "Occasional", "At-Risk"]

    for i, cluster in enumerate(profile.index):
        segment_map[cluster] = labels[i]

    rfm['Segment'] = rfm['Cluster'].map(segment_map)

    return rfm, kmeans, scaler
