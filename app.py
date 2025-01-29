import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load the trained model (ensure it's in the same directory)
model = load("trained_model.joblib")

# Streamlit App Title with Emoji
st.title("🏡 House Price Prediction")
st.image("https://www.realtor.com/research/wp-content/uploads/sites/3/2020/06/houses-image.jpg",  use_container_width=True)
st.write("🔍 Enter the details below to get an estimated house price!")

# User Input Features with Icons
MSSubClass = st.number_input("🏠 MSSubClass", min_value=0, step=1)
MSZoning = st.selectbox("📌 MSZoning", options=["RL", "RM", "C (all)", "FV", "RH"])
LotArea = st.number_input("📏 LotArea (sq ft)", min_value=500, step=50)
LotConfig = st.selectbox("🏡 LotConfig", options=["Inside", "FR2", "Corner", "CulDSac", "FR3"])
BldgType = st.selectbox("🏗️ Building Type", options=["1Fam", "2fmCon", "Duplex", "TwnhsE", "Twnhs"])
OverallCond = st.slider("🔧 Overall Condition", min_value=1, max_value=10, step=1)
YearBuilt = st.number_input("📅 Year Built", min_value=1800, max_value=2025, step=1)
YearRemodAdd = st.number_input("🔄 Year Remodeled", min_value=1800, max_value=2025, step=1)
Exterior1st = st.selectbox("🛠️ Exterior Material", options=["VinylSd", "HdBoard", "MetalSd", "Wd Sdng", "Plywood", "CemntBd"])
BsmtFinSF2 = st.number_input("🏗️ Basement Fin SF2", min_value=0, step=50)
TotalBsmtSF = st.number_input("📐 Total Basement SF", min_value=0, step=50)

# Convert categorical features to numerical using label encoding
encoding_map = {
    "MSZoning": {"RL": 0, "RM": 1, "C (all)": 2, "FV": 3, "RH": 4},
    "LotConfig": {"Inside": 0, "FR2": 1, "Corner": 2, "CulDSac": 3, "FR3": 4},
    "BldgType": {"1Fam": 0, "2fmCon": 1, "Duplex": 2, "TwnhsE": 3, "Twnhs": 4},
    "Exterior1st": {"VinylSd": 0, "HdBoard": 1, "MetalSd": 2, "Wd Sdng": 3, "Plywood": 4, "CemntBd": 5}
}

input_data = pd.DataFrame({
    "MSSubClass": [MSSubClass],
    "MSZoning": [encoding_map["MSZoning"][MSZoning]],
    "LotArea": [LotArea],
    "LotConfig": [encoding_map["LotConfig"][LotConfig]],
    "BldgType": [encoding_map["BldgType"][BldgType]],
    "OverallCond": [OverallCond],
    "YearBuilt": [YearBuilt],
    "YearRemodAdd": [YearRemodAdd],
    "Exterior1st": [encoding_map["Exterior1st"][Exterior1st]],
    "BsmtFinSF2": [BsmtFinSF2],
    "TotalBsmtSF": [TotalBsmtSF]
})

# Prediction Button with Animation
if st.button("🚀 Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Estimated House Price: ${prediction[0]:,.2f}")
        st.balloons()
    except ValueError as e:
        st.error(f"⚠️ Error in prediction: {str(e)}. Please check the input values.")
