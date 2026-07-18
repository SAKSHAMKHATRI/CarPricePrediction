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
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.main-title{
    font-size:42px;
    font-weight:700;
    text-align:center;
}

.sub-title{
    text-align:center;
    color:#9ca3af;
    font-size:18px;
    margin-bottom:30px;
}

.result-box{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    text-align:center;
    border:1px solid #334155;
}

.result-price{
    font-size:36px;
    font-weight:bold;
    color:#00E676;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

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
car_data = df[
    (df["brand"] == brand) &
    (df["model"] == model_name)
]
st.markdown("### 🚘 Car Specifications")
fuel_type = car_data["fuel_type"].mode()[0]
seller_type = car_data["seller_type"].mode()[0]
transmission_type = car_data["transmission_type"].mode()[0]

mileage = car_data["mileage"].mean()
engine = car_data["engine"].mean()
max_power = car_data["max_power"].mean()

seats = int(car_data["seats"].mode()[0])

col1, col2 = st.columns(2)

col1, col2 = st.columns(2)

with col1:
    st.metric("⛽ Fuel Type", fuel_type)
    st.metric("⚙️ Transmission", transmission_type)
    st.metric("💺 Seats", seats)

with col2:
    st.metric("🔧 Engine", f"{engine:.0f} CC")
    st.metric("⚡ Max Power", f"{max_power:.0f} bhp")
    st.metric("🛣️ Mileage", f"{mileage:.2f} km/l")

# Predict Button
predict = st.button(
    "🚀 Predict Selling Price",
    use_container_width=True
)

if predict:

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
        st.markdown(f"""
<div class="result-box">
    <h3>💰 Estimated Selling Price</h3>
    <div class="result-price">
        ₹ {prediction:,.0f}
    </div>
</div>
""", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction Error: {e}")


st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:gray;'>Developed by <b>Saksham Khatri</b></div>",
    unsafe_allow_html=True
)