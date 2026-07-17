import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/car_price_model.joblib")

# Load dataset
df = pd.read_csv("data/cardekho_dataset.csv")

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details below to predict its selling price.")
# Brand Dropdown
brands = sorted(df["brand"].unique())

brand = st.selectbox(
    "Select Brand",
    brands
)
# Model Dropdown (based on selected brand)
models = sorted(
    df[df["brand"] == brand]["model"].unique()
)

model_name = st.selectbox(
    "Select Model",
    models
)
# Vehicle Age
vehicle_age = st.number_input(
    "Vehicle Age (Years)",
    min_value=0,
    max_value=30,
    value=5
)

# KM Driven
km_driven = st.number_input(
    "KM Driven",
    min_value=0,
    value=50000,
    step=1000
)

# Fuel Type
fuel_type = st.selectbox(
    "Fuel Type",
    sorted(df["fuel_type"].unique())
)

# Seller Type
seller_type = st.selectbox(
    "Seller Type",
    sorted(df["seller_type"].unique())
)

# Transmission Type
transmission_type = st.selectbox(
    "Transmission Type",
    sorted(df["transmission_type"].unique())
)

# Mileage
mileage = st.number_input(
    "Mileage (km/l)",
    min_value=0.0,
    value=20.0,
    step=0.1
)

# Engine
engine = st.number_input(
    "Engine (CC)",
    min_value=500,
    max_value=7000,
    value=1200,
    step=100
)

# Max Power
max_power = st.number_input(
    "Max Power (bhp)",
    min_value=20.0,
    max_value=700.0,
    value=80.0,
    step=1.0
)

# Seats
seats = st.number_input(
    "Seats",
    min_value=2,
    max_value=10,
    value=5,
    step=1
)
# Predict Button
# Predict Button
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "brand": [brand],
        "model": [model_name],
        "vehicle_age": [vehicle_age],
        "km_driven": [km_driven],
        "seller_type": [seller_type],
        "fuel_type": [fuel_type],
        "transmission_type": [transmission_type],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats]
    })

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated Selling Price: ₹ {prediction:,.0f}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
    