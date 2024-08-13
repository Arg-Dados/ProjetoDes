# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, 'vendas.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outfiles')
CHUNK_SIZE = 10**6  # 1 milhão de linhas por chunk
