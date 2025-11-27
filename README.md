# CrediSight – AI-Driven Loan Underwriting & Portfolio Risk Management System

CrediSight is an end-to-end credit risk scoring and lending portfolio analytics system built using Python, Streamlit, SQL, and real LendingClub 2007–2018 data.  
It simulates how digital lenders evaluate borrowers, manage portfolio risk, and make data-driven underwriting decisions.

---

## 🚀 Features

### **1. Machine Learning–Based Underwriting Engine**
- Predicts **Probability of Default (PD)** using borrower attributes (income, DTI, FICO, credit lines, inquiries, loan amount, etc.)
- Generates **Approve/Reject** decisions
- Recommends a **safe loan amount** based on risk  
- Trained using LendingClub accepted loans dataset

### **2. Interactive Loan Application Scoring**
- Streamlit UI form for entering applicant details  
- Sliders to vary loan amount and instantly observe PD changes  
- File upload to score multiple applications in bulk  
- Decisions stored into:
  - `accepted_loans`
  - `rejected_loans`

### **3. Portfolio Monitoring Dashboard (MIS)**
- Total disbursements, active loans, closed loans, defaults  
- **NPA%, PAR30/60/90, default trends**  
- Distribution by purpose, grade, income, geography  
- Early-warning indicators (delinquency, utilization spikes)  
- Dynamic filters and time-based analysis

### **4. SQL-Backed Lending Database**
- PostgreSQL / SQL Server used for:
  - Application storage  
  - Approved/rejected loan records  
  - Portfolio MIS calculations  
- All actions execute SQL queries directly

### **5. Batch Model Retraining (Manual)**
- Fetch latest loan data from DB  
- Retrain ML model  
- Evaluate updated metrics (AUC, KS, Bad Rate)  
- Save new `model.pkl` for dashboard inference  
- (Future) Add automated retrain & model versioning

---

## 🧮 Machine Learning Overview

### **Models**
- Logistic Regression (baseline)  
- XGBoost (final model)

### **Feature Engineering**
- DTI normalization  
- Credit utilization metrics  
- FICO range features  
- Age of credit lines  
- Inquiry & delinquency indicators  
- Installment-to-income ratio  
- Purpose encoding  
- Employment length buckets  

### **Evaluation**
- AUC  
- KS Statistic  
- Bad Rate separation  
- Confusion matrix  
- Calibration curve  

---

## 📊 Streamlit Dashboard Modules

### **1. Underwriting Engine**
- Applicant input  
- PD prediction  
- Decision (Approve/Reject)  
- Recommended loan amount  
- Store into DB  

### **2. Portfolio MIS**
- KPIs  
- Trend charts  
- Vintage curves  
- Purpose/state analysis  
- Risk flag monitoring  

### **3. Risk Simulation**
- Loan amount vs PD  
- DTI / income sensitivity  
- Risk appetite scenarios  

---

## 🛠️ Tech Stack
- **Python** (pandas, numpy, scikit-learn, xgboost)  
- **Streamlit** (UI & dashboard)  
- **SQL Server **  
- **Matplotlib / Plotly**  
- **Joblib** (model storage)

---

## 🚧 Future Enhancements
- Automated model retraining pipeline  
- Hosting remote
- Real-time scoring API 
- Collections & recovery analytics  

---

