import streamlit as st
import pandas as pd
from joblib import load
import urllib.request

# Load model from an external URL
url = "https://raw.githubusercontent.com/yourusername/House_pred/main/trained_model.joblib"
urllib.request.urlretrieve(url, "trained_model.joblib")

model = load("trained_model.joblib")

st.title("🏡 House Price Prediction")

lot_size = st.number_input("Lot Size (sq ft)", value=500)
num_rooms = st.slider("Number of Rooms", 1, 10, 3)

if st.button("Predict Price"):
    prediction = model.predict([[lot_size, num_rooms]])
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
