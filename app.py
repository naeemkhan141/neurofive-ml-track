import streamlit as st
import joblib
import pandas as pd

model = joblib.load('simple_churn_model.pkl')

st.title("Customer Churn Predictor")
st.write("Customer ki details daalo aur pata karo ke wo company chhod sakta hai ya nahi.")

tenure = st.number_input("Tenure (kitne mahine se customer hai)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, value=70.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    })
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Ye customer churn kar sakta hai (Risk: {probability:.1%})")
    else:
        st.success(f"✅ Ye customer likely stay karega (Risk: {probability:.1%})")
