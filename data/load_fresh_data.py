from database import Database  
import os
from dotenv import load_dotenv 

load_dotenv()  

db = Database(server=os.getenv("DB_SERVER"), database=os.getenv("DB_DATABASE"))

output_dir = "raw"
os.makedirs(output_dir, exist_ok=True)

accepted_df = db.fetch("SELECT * FROM AcceptedCredit")
accepted_csv_path = os.path.join(output_dir, "accepted.csv")
accepted_df.to_csv(accepted_csv_path, index=False)
print(f"AcceptedCredit saved to {accepted_csv_path}")

rejected_df = db.fetch("SELECT * FROM RejectedCredit")
rejected_csv_path = os.path.join(output_dir, "rejected.csv")
rejected_df.to_csv(rejected_csv_path, index=False)
print(f"RejectedCredit saved to {rejected_csv_path}")