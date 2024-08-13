from data_ingestion import ingest_data

if __name__ == '__main__':
    for chunk in ingest_data():
        print(f"Processed a chunk with {len(chunk)} rows.")
