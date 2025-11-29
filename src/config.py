import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    RAW_REJECTED = os.path.join(DATA_DIR, "raw/rejected.csv")
    RAW_ACCEPTED = os.path.join(DATA_DIR, "raw/accepted.csv")

    PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
    MODEL_DIR = os.path.join(BASE_DIR, "models")
    BATCH_SIZE = 50000   

    TARGET_COLUMN = "loan_status"

config = Config()