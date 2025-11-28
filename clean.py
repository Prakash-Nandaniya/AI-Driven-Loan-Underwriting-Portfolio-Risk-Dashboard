import pandas as pd

# Path to the CSV file
csv_file = r"C:\Code\AI-Driven-Loan-Underwriting-Portfolio-Risk-Dashboard\data\raw\rejected_2007_to_2018q4\rejected_2007_to_2018Q4.csv"

# Read CSV safely
df = pd.read_csv(csv_file, dtype=str)  # read all columns as string to avoid type errors

# Strip spaces from headers and values
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Replace any newline, tab, or problematic characters in text columns
text_columns = ['Loan Title', 'Debt-To-Income Ratio', 'Zip Code', 'State', 'Employment Length']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].str.replace(r'[\n\r\t]', ' ', regex=True)

# Replace commas inside text columns to avoid CSV parsing issues
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].str.replace(',', ';')  # replace commas with semicolon

# Overwrite the same CSV file with cleaned data (UTF-8 without BOM)
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f"CSV file cleaned and updated: {csv_file}")
