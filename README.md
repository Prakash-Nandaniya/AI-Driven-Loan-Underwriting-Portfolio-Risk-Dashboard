# CrediSight – AI-Driven Loan Underwriting & Portfolio Risk Management System

An end-to-end credit risk scoring, underwriting decision engine, and lending portfolio analytics dashboard built using Python, Streamlit, SQL, and real-world LendingClub 2007–2018 data.

This project simulates how digital lending companies design credit policies, evaluate borrowers, monitor portfolio risk, and automate underwriting workflows — fully aligned with Portfolio Management, Credit Strategy, and Risk Analytics responsibilities described in the role of *Senior Analyst – Risk & Portfolio Mgmt*.  

---

## 🚀 Features

### 🔹 1. **Machine Learning–Based Underwriting Engine**
- Processes borrower application data (loan amount, income, FICO, DTI, purpose, credit lines, inquiries, etc.)
- Predicts **Probability of Default (PD)** using a trained ML model (Logistic Regression / XGBoost)
- Generates **Approve / Reject** decision
- Provides **risk score**, **PD bands**, and **recommended safe loan amount**
- Uses LendingClub’s accepted loans (2007–2018) as training data

### 🔹 2. **Interactive Loan Application Simulation**
- Streamlit UI with:
  - Input fields (income, DTI, FICO, loan amount, tenure, home ownership, etc.)
  - Sliders to vary loan amount and instantly observe PD changes
  - Fix PD threshold and compute the **max loan user can safely be offered**
  - Drop-file option to upload multiple applications and score them in bulk
- After decision, applications are stored in:
  - **accepted_loans** table  
  - **rejected_loans** table  

### 🔹 3. **Portfolio Monitoring MIS**
Tracks portfolio KPIs commonly used in digital lending:
- Total disbursed  
- Active vs closed vs defaulted loans  
- **NPA% / PAR30 / PAR60 / PAR90**  
- **Vintage curves**  
- Risk distribution across grades, income brackets, and geographies  
- Early-warning indicators (delinquency, inquiries, utilization spikes)  
- Filters by purpose, grade, state, loan issue date, and more  
- All dashboards update dynamically based on database data

### 🔹 4. **SQL-Backed Lending Database**
Built using PostgreSQL / SQL Server to practice real analytic workflows:
- `applications`  
- `accepted_loans`  
- `rejected_loans`  
- `model_versions` (future upgrade)  

All actions (approve, reject, score applicants) write directly via SQL.

### 🔹 5. **Model Retraining Workflow (Batch Mode)**
Currently manual (industry-standard):
1. Pull latest DB data  
2. Retrain ML model  
3. Evaluate performance: AUC, KS, Bad Rate, PSI  
4. Save updated `model.pkl`  
5. Dashboard uses the new model automatically  

A future upgrade adds:
- Streamlit **"Retrain Model"** button  
- Automated batch retrain scripts  
- Model versioning  

---

## 🧠 Why This Project Matches Digital Lending Roles

This project directly demonstrates skills required for **Risk & Portfolio Mgmt**:  
✔ Credit strategy development  
✔ Building lending decision models  
✔ Portfolio performance monitoring  
✔ Data cleaning & feature engineering  
✔ SQL automation  
✔ Test-and-learn simulation  
✔ Business-driven analytics  
✔ Python, ML, dashboards  
✔ End-to-end process orientation  

(Aligned with the JD: Portfolio Strategy, MIS, Automation, SQL/Python) :contentReference[oaicite:1]{index=1}

---

## 📂 Project Architecture

CrediSight/
│
├── data/
│ ├── accepted_2007_2018.csv
│ ├── rejected_2007_2018.csv
│
├── models/
│ ├── model.pkl
│ ├── train_model.py
│
├── database/
│ ├── schema.sql
│ ├── connection.py
│
├── streamlit_app/
│ ├── app.py
│ ├── pages/
│ │ ├── 1_Underwriting.py
│ │ ├── 2_Portfolio_MIS.py
│ │ ├── 3_Risk_Simulation.py
│
├── utils/
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ ├── scoring.py
│
└── README.md


---

## 🧮 Machine Learning Approach

### **Model Type**
- Logistic Regression (baseline)
- XGBoost (final model)

### **Feature Engineering Includes**
- DTI ratio normalization  
- FICO range compression  
- Utilization metrics  
- Credit line age features  
- Inquiry & delinquency features  
- Past derogatory markers  
- Installment-to-income ratio  
- Loan amount scaling  
- Purpose encoding  
- Employment length bucketization  

### **Evaluation Metrics**
- AUC  
- KS Statistic (industry standard)  
- Bad Rate Separation  
- Confusion matrix  
- Calibration curve  

---

## 📊 Streamlit Dashboard Pages

### **📌 1. Underwriting Engine**
Enter applicant info → model returns:
- Probability of default  
- Approval decision  
- Recommended loan amount  
- Database insert option  

### **📌 2. Portfolio MIS**
- KPIs  
- Trend charts  
- Risk flags  
- Vintage curves  
- Purpose/state distributions  
- Active vs closed vs default status  

### **📌 3. Risk Simulation**
- Vary loan amount  
- Vary income or DTI  
- Observe PD effect  
- Risk appetite scenario tests  

---

## 🗄️ Database Design (SQL)

```sql
CREATE TABLE accepted_loans (...);
CREATE TABLE rejected_loans (...);
CREATE TABLE applications (...);
CREATE TABLE model_versions (...);
Supports SQL queries for MIS and model retraining.
```
🛠️ Tech Stack

Python (pandas, numpy, scikit-learn, xgboost)

Streamlit (dashboard + UI)

SQL Server / PostgreSQL

Matplotlib / Plotly (visual analytics)

Joblib (model persistence)

🚧 Future Enhancements

Automated batch retrain pipeline

Model versioning (MLflow-like approach)

Real-time scoring API (FastAPI)

Early-warning alerts via WhatsApp/Email

Collections risk dashboard

📬 Contact

For questions or collaboration, feel free to reach out!


---

# ⭐ **If you want, I can also create:**

### ✔ Resume project entry (final polished)  
### ✔ GitHub sidebar sections  
### ✔ Diagram for architecture  
### ✔ SQL schema file  
### ✔ Folder boilerplate code  
### ✔ Streamlit page template  
### ✔ Train model pipeline template  

Just tell me and I’ll generate everything.


