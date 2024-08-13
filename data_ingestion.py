import pandas as pd
from config import DATA_PATH, CHUNK_SIZE

def ingest_data():
    for chunk in pd.read_csv(DATA_PATH, chunksize=CHUNK_SIZE):
        yield chunk
