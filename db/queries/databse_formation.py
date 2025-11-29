import os
from ..database import Database
from dotenv import load_dotenv
load_dotenv()  

db = Database(server=os.getenv("DB_SERVER"), database=os.getenv("DB_DATABASE"))

sql_files = [
    'table_creation_accepted.sql',
    'table_creation_rejected.sql',
    'csv_loading_accepted.sql',
    'csv_loading_rejected.sql'
]

sql_folder = r'C:\Code\AI-Driven-Loan-Underwriting-Portfolio-Risk-Dashboard\db\queries'

for file_name in sql_files:
    file_path = os.path.join(sql_folder, file_name)
    print(f"Running {file_name}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    try:
        db.execute(sql_script)
        print(f"{file_name} executed successfully.")
    except Exception as e:
        print(f"Error executing {file_name}: {e}")