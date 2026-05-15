import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("telco_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# creating UI

st.title("Customer Churn Prediction by M")
st.markdown("Enter customer details below:")

# getting input as original df
gender = st.selectbox("Gender", ['Male', 'Female'])
partner = st.selectbox("Have Partner?", ['Yes', 'No'])
dependents = st.selectbox("Dependents", ['Yes', 'No'])
tenure = st.number_input("Tenure (in months)", 0, 80, 35)
phoneservice = st.selectbox("Phone Service", ['Yes', 'No'])
lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
internet = st.selectbox("Internet Service", ['Fiber optic', 'DSL', 'No'])
security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
techsupport = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
streamingtv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
payment = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthlycharges = st.number_input("Monthly Charges", 10, 130, 60)
totalcharges = st.number_input("Total Charges", 10, 9000, 2500)

#
if st.button("Predict"):
    raw_input = {
        'TenureMonths': tenure,
        'MonthlyCharges': monthlycharges,
        'TotalCharges': totalcharges,
        'Gender_' + gender: 1,
        'Partner_' + partner: 1,
        'Dependents_' + dependents: 1,
        'PhoneService_' + phoneservice: 1,
        'MultipleLines_' + lines: 1,
        'InternetService_' + internet: 1,
        'OnlineSecurity_' + security: 1,
        'OnlineBackup_' + backup: 1,
        'DeviceProtection_' + protection: 1,
        'TechSupport_' + techsupport: 1,
        'StreamingTV_' + streamingtv: 1,
        'Contract_' + contract: 1,
        'PaperlessBilling_' + billing: 1,
        'PaymentMethod_' + payment: 1
    }
    
    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    if prediction == 1 :
        st.error("‼️Customer left the company")
    else:
        st.success("✅Customer is still using the service")


    
