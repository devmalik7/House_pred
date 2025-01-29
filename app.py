import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model (ensure it's in the same directory)
model = load("trained_model.joblib")

# Streamlit App Title
st.title("🏡 House Price Prediction")

# User Input Features
lot_size = st.number_input("Lot Size (sq ft)", value=500)
num_rooms = st.slider("Number of Rooms", 1, 10, 3)

# Prediction Button
if st.button("Predict Price"):
   input_data = pd.DataFrame({
    "MSSubClass": [MSSubClass],
    "MSZoning": [MSZoning],
    "LotArea": [LotArea],
    "LotConfig": [LotConfig],
    "BldgType": [BldgType],
    "OverallCond": [OverallCond],
    "YearBuilt": [YearBuilt],
    "YearRemodAdd": [YearRemodAdd],
    "Exterior1st": [Exterior1st],
    "BsmtFinSF2": [BsmtFinSF2],
    "TotalBsmtSF": [TotalBsmtSF]
})

prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
