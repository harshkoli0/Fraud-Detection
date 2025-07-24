import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open("fraud_model.pkl","rb"))

st.title("Fraud Detection Prediction App")

st.markdown("please enter the transaction detailes and use predict button")
st.divider()

transaction_type=st.selectbox("Transaction Type ",["PAYMENT","TRANSFER","CASHOUT","DEPOSIT"])
amount=st.number_input("Amount",min_value=0.0,value=100000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=100000.0, key="sender_old")
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=100000.0, key="sender_new")

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=100000.0, key="receiver_old")
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=100000.0, key="receiver_new")


if st.button("Predict-"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest}])

    
    prediction=model.predict(input_data)
    
    st.subheader(f"prediction: {int(prediction)}")
    
    if prediction==1:
        st.error("this transaction can be fraud")
    else:
        st.success("this transaction looks like it is not fraud")
    
        