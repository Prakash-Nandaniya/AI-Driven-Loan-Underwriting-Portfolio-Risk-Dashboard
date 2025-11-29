import pandas as pd
from config import config
from utils import ensure_dir

def clean_batch(df):
    df = df.dropna(subset=[config.TARGET_COLUMN])
    df = df.fillna(0)
    return df

def clean_data(input_file):
    output_file = f"{config.PROCESSED_DIR}/cleaned.csv"
    ensure_dir(config.PROCESSED_DIR)

    first = True
    for chunk in pd.read_csv(input_file, chunksize=config.BATCH_SIZE):
        cleaned = clean_batch(chunk)
        cleaned.to_csv(output_file, index=False,
                       mode="w" if first else "a",
                       header=first)
        first = False

    return output_file
