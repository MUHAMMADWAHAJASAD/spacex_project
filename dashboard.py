import streamlit as st
import pandas as pd
import pickle

# Title
st.title("🚀 SpaceX Launch Success Predictor")

# Load the trained logistic regression model
with open("model.pkl", "rb") as f:
    logreg = pickle.load(f)

st.subheader("📥 Input Launch Parameters")

# User inputs
latitude = st.number_input("Launchpad Latitude", min_value=-90.0, max_value=90.0, value=28.56)
longitude = st.number_input("Launchpad Longitude", min_value=-180.0, max_value=180.0, value=-80.57)
temp = st.slider("Temperature (°C)", 0, 50, 27)
wind_speed = st.slider("Wind Speed (m/s)", 0, 100, 10)
humidity = st.slider("Humidity (%)", 0, 100, 70)
clouds = st.slider("Cloud Coverage (%)", 0, 100, 50)

st.subheader("🧬 Rocket & Launchpad")
rocket_1 = st.selectbox("Rocket: 5e9d0d95eda69973a809d1ec", [0, 1])
rocket_2 = st.selectbox("Rocket: 5e9d0d95eda69974db09d1ed", [0, 1])
launchpad_1 = st.selectbox("Launchpad: 5e9e4502f509092b78566f87", [0, 1])
launchpad_2 = st.selectbox("Launchpad: 5e9e4502f509094188566f88", [0, 1])
launchpad_3 = st.selectbox("Launchpad: 5e9e4502f5090995de566f86", [0, 1])

st.subheader("🚀 Mission Name")
name_encoded = st.number_input("Name Encoded (e.g. FalconSat → 56)", min_value=0, max_value=500, value=56)

# Predict button
if st.button("Predict Launch Success"):
    # Structure input as a DataFrame to avoid warnings
    input_data = pd.DataFrame([{
        'latitude': latitude,
        'longitude': longitude,
        'temp': temp,
        'wind_speed': wind_speed,
        'humidity': humidity,
        'clouds': clouds,
        'rocket_5e9d0d95eda69973a809d1ec': rocket_1,
        'rocket_5e9d0d95eda69974db09d1ed': rocket_2,
        'launchpad_5e9e4502f509092b78566f87': launchpad_1,
        'launchpad_5e9e4502f509094188566f88': launchpad_2,
        'launchpad_5e9e4502f5090995de566f86': launchpad_3,
        'name_encoded': name_encoded
    }])

    # Make prediction
    prediction = logreg.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.success("✅ Predicted: Launch will likely succeed!")
    else:
        st.error("❌ Predicted: Launch may fail.")
