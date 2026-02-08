# 🚗 Car Price Prediction App
A machine learning web application that predicts the resale price of used cars based on various features like mileage, age, fuel type, and transmission. Built with Scikit-Learn and deployed using Streamlit.

## 📌 Project Overview
Buying or selling a used car can be daunting due to price uncertainty. This project utilizes a Random Forest Regressor model to provide accurate price estimations, helping users make informed financial decisions.

## Key Features:
1. **Predictive Modeling:** Uses a trained Random Forest model for high-accuracy regressions.
2. **Interactive UI:** A clean, user-friendly interface built with Streamlit.
3. **Data Scaling:** Implements robust feature scaling via scaler.pkl to ensure prediction consistency.

## 🛠️ Tech Stack
- **Language:** Python
- **ML Frameworks:** Scikit-Learn, Pandas, NumPy
- **Deployment:** Streamlit
- **Model:** Random Forest Regressor

## 📁 Repository Structure
├── app.py              # Streamlit web application code
├── requirements.txt    # List of required Python packages
├── rf_reg_model        # Trained Random Forest model file
├── scaler.pkl          # Pickled scaler for data preprocessing
└── README.md           # Project documentation

## 🚀 Getting Started
### 1. Clone the repository
git clone https://github.com/Akshayus29/car_price_prediction_streamlit.git
cd car_price_prediction_streamlit

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Application
streamlit run app.py

## 📊 Model Information
The model was trained on a comprehensive dataset of used cars. Preprocessing steps included:
1. **Categorical Encoding:** Converting fuel types and transmission types into numerical values.
2. **Feature Scaling:** Normalizing features like 'Kms_Driven' using a standard scaler.
3. **Optimization:** Hyperparameter tuning to minimize Mean Absolute Error (MAE).

## Demo video of My Web App
https://github.com/user-attachments/assets/c7a7160e-e40b-4039-94e4-266a502b1ec0

## Check out My Web App
[Sample App](https://carpricepredictionapp-site.streamlit.app/)

