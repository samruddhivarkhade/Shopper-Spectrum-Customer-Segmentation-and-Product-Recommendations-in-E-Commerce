# src/data_loader.py

import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="ISO-8859-1")
    return df
