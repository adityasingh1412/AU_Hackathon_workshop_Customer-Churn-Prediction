import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.title("Customer Churn Prediction")

st.write("Enter customer details to predict churn")

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 500.0)

if st.button("Predict"):
    
    # simple example model input
    X = [[tenure, monthly_charges, total_charges]]

    model = LogisticRegression()
    
    # dummy training data (for demo)
    import numpy as np
    X_train = np.random.rand(100,3)
    y_train = np.random.randint(0,2,100)
    
    model.fit(X_train,y_train)

    prediction = model.predict(X)

    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")
