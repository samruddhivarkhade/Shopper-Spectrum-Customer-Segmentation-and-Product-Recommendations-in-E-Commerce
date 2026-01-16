# src/recommender.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def train_recommender(df):
    pivot = df.pivot_table(
        index='CustomerID',
        columns='Description',
        values='Quantity',
        aggfunc='sum'
    ).fillna(0)

    similarity = cosine_similarity(pivot.T)

    item_similarity = pd.DataFrame(
        similarity,
        index=pivot.columns,
        columns=pivot.columns
    )

    return item_similarity


def recommend(product, item_similarity, top_n=5):
    if product not in item_similarity.columns:
        return []

    return (
        item_similarity[product]
        .sort_values(ascending=False)
        .iloc[1:top_n+1]
        .index
        .tolist()
    )
