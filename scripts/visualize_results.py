import pandas as pd
import matplotlib.pyplot as plt
from google.cloud import bigquery

# Path to your JSON key
key_path = r"C:\Users\patra\Downloads\bigquery-key.json"

def query_to_df(query):
    client = bigquery.Client.from_service_account_json(key_path)
    query_job = client.query(query)
    return query_job.to_dataframe()

if __name__ == "__main__":
    query = """
        SELECT 
            FORMAT_DATE('%b', order_date) AS month_name,  -- Jan, Feb, Mar...
            EXTRACT(MONTH FROM order_date) AS month_num, -- For sorting
            SUM(revenue) AS total_revenue
        FROM `billing-project-470408.ecommerce_dataset.sales_data`
        GROUP BY month_name, month_num
        ORDER BY month_num
    """
    df = query_to_df(query)
    print(df.head())

    plt.plot(df["month_name"], df["total_revenue"], marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(True)
    plt.show()
