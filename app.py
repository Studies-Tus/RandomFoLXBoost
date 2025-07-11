import streamlit as st
import cloudpickle
import pandas as pd

# Load the saved model
with open("RFmaize_model(1).pkl", "rb") as f:
    model = cloudpickle.load(f)

st.set_page_config(page_title="Maize Yield Predictor", layout="centered")

st.title("🌽 Maize Yield Prediction App")

# Inputs
soil_type = st.selectbox("Soil Type", ["Loamy", "Sandy", "Silty"])
irrigation = st.selectbox("Irrigation Method", ["Flood", "Manual", "Sprinkler", "Drip"])
region = st.selectbox("Region", ["North", "South", "East", "West"])

rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
soil_ph = st.number_input("Soil pH", min_value=0.0)
fertilizer = st.number_input("Fertilizer Used (kg/ha)", min_value=0.0)
density = st.number_input("Planting Density (plants/m²)", min_value=0.0)

if st.button("Predict"):
    input_df = pd.DataFrame({
        'Soil_Type': [soil_type],
        'Irrigation_Method': [irrigation],
        'Region': [region],
        'Rainfall (mm)': [rainfall],
        'Temperature (°C)': [temperature],
        'Soil_pH': [soil_ph],
        'Fertilizer_Used (kg/ha)': [fertilizer],
        'Planting_Density (plants/m²)': [density]
    })
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Maize Yield: {prediction:.2f} t/ha")
