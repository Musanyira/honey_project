import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("honey_model.pkl")

st.title("🐝 Honey Yield Prediction App")

# User Inputs
rainfall = st.number_input("Rainfall (mm)", 400, 1200, 800)
temperature = st.number_input("Average Temperature (°C)", 20.0, 35.0, 27.0)
humidity = st.number_input("Humidity (%)", 40, 100, 70)
num_hives = st.number_input("Number of Hives", 1, 100, 20)
experience = st.number_input("Experience (years)", 1, 30, 5)
inspection = st.number_input("Inspection Frequency", 1, 15, 4)
disease_status = st.selectbox("Disease Status", ["no", "yes"])

hive_type = st.selectbox("Hive Type", ["traditional", "modern"])
season = st.selectbox("Season", ["dry", "rainy"])
colony_strength = st.selectbox("Colony Strength", ["weak", "medium", "strong"])

if st.button("Predict Honey Yield"):
    
    input_data = pd.DataFrame({
    "rainfall_mm": [rainfall],
    "avg_temperature": [temperature],
    "humidity": [humidity],
    "num_hives": [num_hives],
    "experience_years": [experience],
    "inspection_frequency": [inspection],
    "hive_type": [hive_type],
    "colony_strength": [colony_strength],
    "disease_status": [disease_status]
})


    prediction = model.predict(input_data)
    
    st.success(f"Estimated Honey Yield: {prediction[0]:.2f} kg")
