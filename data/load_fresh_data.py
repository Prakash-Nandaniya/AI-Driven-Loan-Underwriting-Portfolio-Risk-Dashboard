from db.database import Database  
import os
from dotenv import load_dotenv 

load_dotenv()  

db = Database(server=os.getenv("DB_SERVER"), database=os.getenv("DB_DATABASE"))

output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

BATCH = 10000


def export_table(table, csv_path):
    print(f"Exporting {table} → {csv_path}")

    cols = db.get_columns(table)

    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(",".join(cols) + "\n")

    offset = 0

    while True:
        query = f"""
            SELECT *
            FROM {table}
            ORDER BY (SELECT NULL) 
            OFFSET {offset} ROWS 
            FETCH NEXT {BATCH} ROWS ONLY;
        """

        df = db.fetch(query)

        if df.empty:
            break

        df = df[cols]  

        df.to_csv(csv_path, mode="a", header=False, index=False)

        print(f"Written batch: {len(df)} rows (offset={offset})")

        offset += BATCH


    print(f"Completed export: {table}\n")


export_table("AcceptedCredit", os.path.join(output_dir, "accepted.csv"))
export_table("RejectedCredit", os.path.join(output_dir, "rejected.csv"))