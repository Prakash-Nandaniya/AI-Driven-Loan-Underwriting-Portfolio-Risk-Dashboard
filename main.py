csv_path = r"C:\Code\AI-Driven-Loan-Underwriting-Portfolio-Risk-Dashboard\data\raw\rejected_2007_to_2018Q4\rejected_2007_to_2018Q4.csv"

with open(csv_path, "r", encoding="utf-8") as f:
    # Read first two raw lines without using csv.reader
    line1 = f.readline().rstrip("\n")
    line2 = f.readline().rstrip("\n")

print("First row (header):")
print(line1)

print("\nSecond row (raw data):")
print(line2)
