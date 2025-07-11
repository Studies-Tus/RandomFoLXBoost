import streamlit as st
import cloudpickle
import pandas as pd

# Load the saved model
with open("random_forest_maize_model.pkl", "rb") as f:
    model = cloudpickle.load(f)

st.set_page_config(page_title="RandomFoLXBoost", layout="centered")

st.title("🌽RandomFoLXBoost ")
st.subheader("Maize Yield Prediction App")
st.write("Input your farm parameters to predict maize yield.")

# Inputs
soil_type = st.selectbox("Soil Type", ["Clayey", "Loamy", "Sandy", "Silty"])
irrigation = st.selectbox("Irrigation Method", ["Flood", "Manual", "Sprinkler", "Drip"])
region = st.selectbox("Region", ["North East", "North West", "North Central", "South East", "South West", "South South"])

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
    st.success(f"Predicted Maize Yield: {prediction:.2f} tons/ha based on the prevailing conditions")
