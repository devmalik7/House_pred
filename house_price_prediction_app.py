
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from joblib import load

# Load trained model
@st.cache_data
def load_model():
    return load("trained_model.joblib")

model = load_model()

# Title and description
st.title("House Price Prediction App")
st.write("This app predicts house prices based on user input. Adjust the parameters below and get your predictions!")

# User input for house features
MSSubClass = st.number_input("MSSubClass", min_value=0, step=1)
MSZoning = st.selectbox("MSZoning", options=["RL", "RM", "C (all)", "FV", "RH"])
LotArea = st.number_input("LotArea", min_value=500, step=50)
LotConfig = st.selectbox("LotConfig", options=["Inside", "FR2", "Corner", "CulDSac", "FR3"])
BldgType = st.selectbox("BldgType", options=["1Fam", "2fmCon", "Duplex", "TwnhsE", "Twnhs"])
OverallCond = st.slider("Overall Condition", min_value=1, max_value=10, step=1)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, step=1)
YearRemodAdd = st.number_input("Year Remodeled", min_value=1800, max_value=2025, step=1)
Exterior1st = st.selectbox("Exterior First Material", options=["VinylSd", "HdBoard", "MetalSd", "Wd Sdng", "Plywood", "CemntBd"])
BsmtFinSF2 = st.number_input("BsmtFinSF2", min_value=0, step=50)
TotalBsmtSF = st.number_input("Total Basement SF", min_value=0, step=50)

# Create input array for prediction
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

# Display prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"The predicted house price is: ${prediction[0]:,.2f}")
