# Telco Customer Churn Prediction

##  Project Overview
This project predicts whether a telecom customer is likely to churn (leave the service) or not using Machine Learning classification algorithms.

The project includes:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Encoding
- Feature Scaling
- Model Training & Evaluation
- Streamlit Web Application Deployment

The final deployed model allows users to enter customer details and get real-time churn predictions.

---

# Problem Statement

Customer churn is one of the biggest challenges for telecom companies.  
This project helps predict customer churn based on customer demographics, account information, and subscribed services.

The goal is to help businesses:
- Identify customers likely to leave
- Improve customer retention
- Reduce revenue loss

---

# Dataset Information

Dataset used:
- Telco Customer Churn Dataset

The dataset contains customer-related information such as:
- Gender
- Tenure
- Internet Service
- Monthly Charges
- Contract Type
- Payment Method
- Tech Support
- Streaming Services
- And more...

Target Variable:
- `Churn`
  - Yes → Customer leaves
  - No → Customer stays

---

# Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# Project Workflow

## 1. Data Cleaning
- Handled missing values
- Converted data types
- Removed inconsistencies

## 2. Exploratory Data Analysis (EDA)
Performed:
- Count plots
- Histograms
- Correlation analysis
- Customer distribution analysis
- Churn comparison analysis

## 3. Data Preprocessing
- Label Encoding
- One-Hot Encoding
- Feature Scaling using StandardScaler

## 4. Model Building
Trained multiple classification models:
- Logistic Regression
- KNN
- Naive Bayes
- Decision Tree
- SVM

## 5. Model Evaluation
Evaluation metrics used:
- Accuracy Score
- F1 Score
- Confusion Matrix
- Classification Report

## 6. Model Selection
Selected the best-performing model based on accuracy and F1 score.

Best Model:
- Logistic Regression

Accuracy Achieved:
- ~80%

---

# Machine Learning Models Comparison

| Model | Accuracy Score |
|---|---|
| Logistic Regression | 0.809 |
| KNN | 0.761 |
| Naive Bayes | 0.646 |
| Decision Tree | 0.704 |
| SVM | 0.816 |

---

# Project Structure

```bash
customer_churn_model/
│
├── app2.py
├── telco_project8.ipynb
├── telco_model.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── README.md
└── telco_customer_churn_dataset.csv
```

# Run Locally

Install libraries
```bash
pip install -r requirements.txt
```
Run app:
``` bash
streamlit run app2.py
```

# Deployment

This project is deployed using Streamlit Cloud.

---

# Author

Mansi Nakum
