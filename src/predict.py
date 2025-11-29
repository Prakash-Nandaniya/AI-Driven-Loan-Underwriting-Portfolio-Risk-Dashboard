import pandas as pd
import joblib

def load_model():
    return joblib.load("models/model.pkl")

def predict_single(data: dict):
    model = load_model()
    df = pd.DataFrame([data])
    return model.predict(df)[0]
