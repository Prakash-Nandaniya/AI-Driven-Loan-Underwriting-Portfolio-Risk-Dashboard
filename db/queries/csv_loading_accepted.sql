BULK INSERT AcceptedCredit
FROM 'C:\Code\AI-Driven-Loan-Underwriting-Portfolio-Risk-Dashboard\data\raw\accepted_2007_to_2018q4\accepted_2007_to_2018Q4.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',      
    FIRSTROW = 2,
    MAXERRORS = 0,
    TABLOCK,
    FORMAT = 'CSV'             
);