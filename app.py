import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="California Housing Price Predictor",
    page_icon="🌴",
    layout="centered",
)

# Custom CSS Styling
st.markdown("""
<style>


/* Buttons */
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    font-size: 1.1rem;
}

div.stButton > button:hover {
    background-color: #45A049;
}

/* Title */
.title {
    font-size: 2.5rem;
    color: #2C3E50;
    text-align: center;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    color: #7f8c8d;
    text-align: center;
    margin-bottom: 30px;
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<div class='title'> California Housing Price Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter housing details below to estimate property price</div>", unsafe_allow_html=True)

# Load model + scaler
model = joblib.load("ridge.pkl")
scaler = joblib.load("scaler.pkl")

# Input card
with st.container():
    st.markdown("<div class='big-card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        longitude = st.number_input("📍 Longitude")
        housing_median_age = st.number_input(" 🏘 Housing Median Age")
        total_rooms = st.number_input("🚪 Total Rooms")
        population = st.number_input("👥 Population")

    with col2:
        latitude = st.number_input("🌍 Latitude")
        total_bedrooms = st.number_input("🛏 Total Bedrooms")
        households = st.number_input("🏘 Households")
        median_income = st.number_input("💰 Median Income")

    is_predict_clicked = st.button("Predict House Price")

    st.markdown("</div>", unsafe_allow_html=True)

# Creating input df
input_df = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income]
})

# Predict
if is_predict_clicked:
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)

    st.success(f"💵 **Predicted House Price:  ${prediction[0]:,.2f}**")
