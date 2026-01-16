# src/data_cleaning.py

import pandas as pd


def clean_data(df):
    # Remove missing CustomerID
    df = df.dropna(subset=['CustomerID'])

    # Remove cancelled invoices
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

    # Remove invalid quantity & price
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # Convert InvoiceDate
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Total price
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df
