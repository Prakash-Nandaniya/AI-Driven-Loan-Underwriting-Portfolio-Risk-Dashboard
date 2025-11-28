BULK INSERT dbo.big_data
FROM 'C:\Code\AI-Driven-Loan-Underwriting-Portfolio-Risk-Dashboard\data\raw\accepted_2007_to_2018q4.csv\accepted_2007_to_2018Q4.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK
);
