import pandas as pd
from sklearn.metrics import classification_report
import joblib
from config import config

def evaluate_model(feature_file):
    model = joblib.load(f"{config.MODEL_DIR}/model.pkl")
    df = pd.read_csv(feature_file, nrows=100000)

    X = df.drop(columns=[config.TARGET_COLUMN])
    y = df[config.TARGET_COLUMN]

    preds = model.predict(X)
    report = classification_report(y, preds)

    print(report)
    return report
