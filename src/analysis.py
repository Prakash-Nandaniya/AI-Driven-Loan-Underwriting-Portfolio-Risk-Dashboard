import pandas as pd

def quick_eda(file):
    df = pd.read_csv(file, nrows=200000)
    print(df.describe())
    print(df.isna().sum())
