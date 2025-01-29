import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load the trained model (ensure it's in the same directory)
model = load("trained_model.joblib")

# Streamlit App Title
st.title("🏡 House Price Prediction")

# User Input Features
lot_size = st.number_input("Lot Size (sq ft)", value=500)
num_rooms = st.slider("Number of Rooms", 1, 10, 3)

# Ensure input is in the correct format for prediction
input_data = np.array([[lot_size, num_rooms]])

# Prediction Button
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
    except ValueError as e:
        st.error(f"Error in prediction: {str(e)}. Please check the input values.")
