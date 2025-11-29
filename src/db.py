import sqlite3

def get_conn():
    return sqlite3.connect("db/credit.db")

def save_predictions(df):
    conn = get_conn()
    df.to_sql("predictions", conn, if_exists="append", index=False)
    conn.close()
