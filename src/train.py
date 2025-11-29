import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from config import config
from utils import ensure_dir

def load_small_train_sample(file):
    # Take only 5% random sample for training
    df = pd.read_csv(file, nrows=500000)
    return df

def train_model(feature_file):
    ensure_dir(config.MODEL_DIR)

    df = load_small_train_sample(feature_file)

    X = df.drop(columns=[config.TARGET_COLUMN])
    y = df[config.TARGET_COLUMN]

    model = RandomForestClassifier(n_estimators=200)
    model.fit(X, y)

    model_path = f"{config.MODEL_DIR}/model.pkl"
    joblib.dump(model, model_path)

    return model_path
