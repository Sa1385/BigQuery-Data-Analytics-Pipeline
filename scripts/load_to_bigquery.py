from google.cloud import bigquery

def load_csv_to_bq(dataset_id, table_id, gcs_uri):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True
    )
    load_job = client.load_table_from_uri(gcs_uri, table_ref, job_config=job_config)
    load_job.result()
    print(f"✅ Loaded data from {gcs_uri} into {dataset_id}.{table_id}")

if __name__ == "__main__":
    load_csv_to_bq("your_dataset", "sales_data", "gs://your-gcs-bucket/datasets/sales_data.csv")
