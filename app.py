import streamlit as st
import pandas as pd
import pickle

# Set page configuration
st.set_page_config(page_title="Car Price Predictor", layout="centered")

# Load the saved model and scaler
try:
    model = pickle.load(open('rf_reg_model', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model or Scaler file not found! Please ensure 'rf_reg_model' and 'scaler.pkl' are in the project folder.")

st.title("🚗 Car Selling Price Prediction")
st.markdown("Enter car details to predict the estimated selling price.")

# Layout with two columns for inputs
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Purchase", min_value=2000, max_value=2024, value=2015)
    present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0, value=5.0)
    kms_driven = st.number_input("Kms Driven", min_value=0, value=20000)

with col2:
    owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

# Button to trigger prediction
if st.button("Predict Selling Price"):
    # Encoding Categorical Features (matching your get_dummies logic)
    fuel_diesel = 1 if fuel_type == "Diesel" else 0
    fuel_petrol = 1 if fuel_type == "Petrol" else 0
    seller_individual = 1 if seller_type == "Individual" else 0
    transmission_manual = 1 if transmission == "Manual" else 0
    
    # Create DataFrame for prediction (must match X_train columns order)
    input_df = pd.DataFrame([[
        year, present_price, kms_driven, owner, 
        fuel_diesel, fuel_petrol, seller_individual, transmission_manual
    ]], columns=['Year', 'Present_Price', 'Kms_Driven', 'Owner', 
                 'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Seller_Type_Individual', 'Transmission_Manual'])
    
    # Scale numerical features (Year, Present_Price, Kms_Driven, Owner)
    num_cols = ['Year', 'Present_Price', 'Kms_Driven', 'Owner']
    input_df[num_cols] = scaler.transform(input_df[num_cols])
    
    # Perform prediction
    prediction = model.predict(input_df)
    
    # Output result
    output = round(prediction[0], 2)
    if output < 0:
        st.warning("The predicted price is negligible (close to zero).")
    else:
        st.success(f"### Estimated Selling Price: ₹{output} Lakhs")