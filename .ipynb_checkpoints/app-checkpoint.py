import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/model.pkl")

# Load feature order
features = joblib.load("model/features.pkl")

st.title("🚗 Used Car Price Prediction")

st.write("Enter the car details below:")

# User Inputs
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
car_age = st.number_input("Car Age (years)", min_value=0)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])


if st.button("Predict Price"):

    # Create input dictionary
    input_dict = {
        "Present_Price": present_price,
        "Kms_Driven": kms_driven,
        "Owner": owner,
        "Car_Age": car_age,
        "Fuel_Type_Diesel": 1 if fuel_type == "Diesel" else 0,
        "Seller_Type_Individual": 1 if seller_type == "Individual" else 0,
        "Transmission_Manual": 1 if transmission == "Manual" else 0
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure correct feature order
    input_df = input_df.reindex(columns=features, fill_value=0)

    # Prediction
    prediction = model.predict(input_df)

    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")