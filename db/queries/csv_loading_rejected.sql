BULK INSERT RejectedCredit
FROM 'C:\Code\AI-Driven-Loan-Underwriting-Portfolio-Risk-Dashboard\data\raw\rejected_2007_to_2018q4\rejected_2007_to_2018Q4.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0d0a',
    FIRSTROW = 2,
    MAXERRORS = 100,
    TABLOCK
);