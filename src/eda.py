import matplotlib.pyplot as plt
import seaborn as sns

def plot_country_distribution(df):
    df['Country'].value_counts().head(10).plot(kind='bar')
    plt.title("Top Countries by Transactions")
    plt.show()


def plot_top_products(df):
    top_products = (
        df.groupby('Description')['Quantity']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    top_products.plot(kind='barh')
    plt.title("Top Selling Products")
    plt.show()


def plot_sales_trend(df):
    df.set_index('InvoiceDate')['TotalPrice'].resample('M').sum().plot()
    plt.title("Monthly Sales Trend")
    plt.show()


def plot_rfm_distribution(rfm):
    rfm[['Recency', 'Frequency', 'Monetary']].hist(bins=20, figsize=(10,6))
    plt.show()
