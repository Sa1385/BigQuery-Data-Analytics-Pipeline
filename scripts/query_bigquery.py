from google.cloud import bigquery

def run_query(sql_file):
    client = bigquery.Client()
    with open(sql_file, "r") as f:
        query = f.read()
    query_job = client.query(query)
    results = query_job.result()
    for row in results:
        print(dict(row))

if __name__ == "__main__":
    run_query("bq_queries/sales_summary.sql")
