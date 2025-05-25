import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="🚀 SpaceX Launch Success Predictor")
st.title("🚀 SpaceX Launch Success Predictor")

st.markdown("Fill in the launch parameters to predict the success of a SpaceX mission:")

# === Input fields ===
latitude = st.number_input("Launchpad Latitude", min_value=-90.0, max_value=90.0, value=28.56)
longitude = st.number_input("Launchpad Longitude", min_value=-180.0, max_value=180.0, value=-80.57)
temp = st.slider("Temperature (°C)", 0, 50, 27)
wind_speed = st.slider("Wind Speed (m/s)", 0, 100, 10)
humidity = st.slider("Humidity (%)", 0, 100, 70)
clouds = st.slider("Cloud Coverage (%)", 0, 100, 50)

# Rocket options (one-hot encoded)
rocket = st.selectbox("Rocket", ["5e9d0d95eda69973a809d1ec", "5e9d0d95eda69974db09d1ed"])
rocket_1 = 1 if rocket == "5e9d0d95eda69973a809d1ec" else 0
rocket_2 = 1 if rocket == "5e9d0d95eda69974db09d1ed" else 0

# Launchpad options
launchpad = st.selectbox("Launchpad", [
    "5e9e4502f509092b78566f87", 
    "5e9e4502f509094188566f88", 
    "5e9e4502f5090995de566f86"
])
launchpad_1 = 1 if launchpad == "5e9e4502f509092b78566f87" else 0
launchpad_2 = 1 if launchpad == "5e9e4502f509094188566f88" else 0
launchpad_3 = 1 if launchpad == "5e9e4502f5090995de566f86" else 0

# Encoded name value
name_encoded = st.number_input("Encoded Mission Name", min_value=0, max_value=200, value=56)

# === Prediction ===
if st.button("Predict Launch Success"):
    input_data = np.array([[
        latitude, longitude, temp, wind_speed, humidity, clouds,
        rocket_1, rocket_2,
        launchpad_1, launchpad_2, launchpad_3,
        name_encoded
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The launch is likely to be **successful**!")
    else:
        st.error("❌ The launch is likely to **fail**.")

