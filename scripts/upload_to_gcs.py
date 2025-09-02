from google.cloud import storage

def upload_to_gcs(bucket_name, source_file, destination_blob):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    print(f"✅ Uploaded {source_file} to gs://{bucket_name}/{destination_blob}")

if __name__ == "__main__":
    upload_to_gcs("your-gcs-bucket", "data/sales_data.csv", "datasets/sales_data.csv")
