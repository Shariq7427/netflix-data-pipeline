import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(BASE_DIR, "input", "netflix_titles.csv")

PARQUET_OUTPUT = os.path.join(BASE_DIR, "output", "parquet")

TRANSFORMED_OUTPUT = os.path.join(BASE_DIR, "output", "transformed")