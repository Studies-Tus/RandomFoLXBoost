# 🌽 Maize Yield Prediction App

This project uses a machine learning model (Random Forest) to predict maize yield (in tons per hectare) based on key environmental and farming inputs.

Built with **Streamlit**, this app allows users such as farmers, agronomists, and researchers to interactively estimate crop yields based on real-world data.

---

## 🚀 Live Demo

👉 [Click here to try the app](#) *(Add your Streamlit Cloud URL here once deployed)*

---

## 💡 Features

- Predict maize yield using:
  - Soil Type
  - Irrigation Method
  - Region
  - Rainfall (mm)
  - Temperature (°C)
  - Soil pH
  - Fertilizer Used (kg/ha)
  - Planting Density (plants/m²)
- Powered by a tuned Random Forest model
- Clean and interactive user interface via Streamlit

---

## 🧠 Model Info

The model was trained on a Nigerian maize dataset and fine-tuned using `GridSearchCV` with 5-fold cross-validation.  
Best parameters:
```python
{
  'n_estimators': 200,
  'max_depth': 10,
  'min_samples_split': 2
}
