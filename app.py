import streamlit as st
import numpy as np
import pandas as pd
import cloudpickle


with open("random_forest_maize_model.pkl", "wb") as f:
    cloudpickle.dump(grid_search.best_estimator_, f)


st.set_page_config(page_title="Maize Yield Predictor", layout="centered")

st.title("🌽 Maize Yield Prediction App")
st.markdown("Enter field parameters below to estimate maize yield (t/ha).")

# User Inputs
soil_type = st.selectbox("Soil Type", ["Loamy", "Sandy", "Silty"])
irrigation = st.selectbox("Irrigation Method", ["Flood", "Manual", "Sprinkler", "Drip"])
region = st.selectbox("Region", ["North", "South", "East", "West"])

rainfall = st.number_input("Rainfall (mm)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
soil_ph = st.number_input("Soil pH", min_value=0.0)
fertilizer = st.number_input("Fertilizer Used (kg/ha)", min_value=0.0)
density = st.number_input("Planting Density (plants/m²)", min_value=0.0)

if st.button("Predict Yield"):
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
    st.success(f"🌾 Predicted Maize Yield: **{prediction:.2f} t/ha**")
