import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model (make sure the model is in the same folder or provide full path)
model = joblib.load('best_model.pkl')

# Function to take user input
def user_input():
    # Define input fields for user to fill in
    rainfall = st.slider('Rainfall (mm)', 0, 300, 100)
    hive_type = st.selectbox('Hive Type', ['None', 'Langstroth', 'Top-Bar', 'Traditional'])
    colony_strength = st.selectbox('Colony Strength', ['None', 'Weak', 'Medium', 'Strong'])
    feeding_type = st.selectbox('Feeding Type', ['None', 'Pollen Patties', 'Sugar Syrup', 'Protein Supplement'])
    disease_status = st.selectbox('Disease Status', ['None', 'Healthy', 'Foulbrood', 'Varroa Mites', 'Nosema'])
    forage_availability = st.selectbox('Forage Availability', ['None', 'Low', 'Medium', 'High'])
    season = st.selectbox('Season', ['None', 'Dry', 'Rainy', 'Transitional'])
    
    # Create a dictionary from the inputs
    input_data = {
        'Rainfall_mm': rainfall,
        'Hive_Type_Top-Bar': 1 if hive_type == 'Top-Bar' else 0,
        'Hive_Type_Traditional': 1 if hive_type == 'Traditional' else 0,
        'Colony_Strength_Strong': 1 if colony_strength == 'Strong' else 0,
        'Colony_Strength_Weak': 1 if colony_strength == 'Weak' else 0,
        'Feeding_Type_Protein Supplement': 1 if feeding_type == 'Protein Supplement' else 0,
        'Feeding_Type_Sugar Syrup': 1 if feeding_type == 'Sugar Syrup' else 0,
        'Disease_Status_Healthy': 1 if disease_status == 'Healthy' else 0,
        'Disease_Status_Nosema': 1 if disease_status == 'Nosema' else 0,
        'Disease_Status_Varroa Mites': 1 if disease_status == 'Varroa Mites' else 0,
        'Forage_Availability_Low': 1 if forage_availability == 'Low' else 0,
        'Forage_Availability_Medium': 1 if forage_availability == 'Medium' else 0,
        'Season_Rainy': 1 if season == 'Rainy' else 0,
        'Season_Transitional': 1 if season == 'Transitional' else 0
    }

    # Convert input data into a DataFrame
    input_df = pd.DataFrame(input_data, index=[0])
    return input_df

# Streamlit title
st.title('Honey Yield Prediction Model')

# Get user input
input_df = user_input()

# Make predictions with the model
prediction = model.predict(input_df)

# Show the prediction result
st.write(f"Predicted Honey Yield: {prediction[0]} kg")






