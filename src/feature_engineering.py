import pandas as pd
from config import config

def process_features(df):
    df["loan_to_income"] = df["loan_amount"] / (df["income"] + 1)
    return df

def apply_feature_engineering(input_file):
    output = f"{config.PROCESSED_DIR}/features.csv"
    first = True

    for chunk in pd.read_csv(input_file, chunksize=config.BATCH_SIZE):
        engineered = process_features(chunk)
        engineered.to_csv(output, index=False,
                          mode="w" if first else "a",
                          header=first)
        first = False

    return output
