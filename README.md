# 💳 Fraud Detection App

This project is a **Machine Learning-based fraud detection system** designed to identify potentially fraudulent transactions. It includes:

The Fraud Detection App is a machine learning-powered web application built using Streamlit that identifies potentially fraudulent financial transactions in real time. By analyzing key transaction features like amount, balance before and after transactions, and transaction type, the app uses a trained Random Forest Classifier to accurately predict whether a transaction is fraudulent or legitimate.

🔗 **Try the app here**:  
👉 [https://fraud-detection-pwjnecpyiz8uonsxcvxqdb.streamlit.app/](https://fraud-detection-pwjnecpyiz8uonsxcvxqdb.streamlit.app/)


- A trained ML model (`RandomForestClassifier`) using transactional data.
- A `Streamlit` web app for real-time prediction.
- Cleaned and structured data pipeline using `pandas`, `scikit-learn`, and `joblib`.


---

## 🚀 Features

- Predicts whether a transaction is fraudulent or legitimate
- Supports user input via a Streamlit form
- Displays prediction results instantly
- Handles transaction types like `PAYMENT`, `TRANSFER`, `CASHOUT`, and `DEPOSIT`

---

## 🧠 Model Overview

The model is trained using the following features:

- `type` — Transaction type (categorical)
- `amount` — Transaction amount
- `oldbalanceOrg` — Sender's balance before transaction
- `newbalanceOrig` — Sender's balance after transaction
- `oldbalanceDest` — Receiver's balance before transaction
- `newbalanceDest` — Receiver's balance after transaction

Model Pipeline:
- Preprocessing: `OneHotEncoder` + `StandardScaler`
- Classifier: `RandomForestClassifier`
- Entire pipeline serialized using `joblib` into `fraud.pkl`

---

## 📦 Installation

### ⚙️ Requirements

```bash
pip install -r requirements.txt
