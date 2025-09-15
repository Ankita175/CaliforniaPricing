import streamlit as st
import numpy as np
import pickle

# Load the saved model and scaler
model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
# Save your scaler similarly or reuse StandardScaler()

st.title("California Housing Price Predictor")
st.write("""
Enter details of the house features to predict the median house price.
""")

# Input features
longitude = st.number_input('Longitude', value=-122.23)
latitude = st.number_input('Latitude', value=37.88)
housing_median_age = st.number_input('Housing Median Age', min_value=0, max_value=100, value=41)
total_rooms = st.number_input('Total Rooms', min_value=0, value=880)
total_bedrooms = st.number_input('Total Bedrooms', min_value=0, value=129)
population = st.number_input('Population', min_value=0, value=322)
households = st.number_input('Households', min_value=0, value=126)
median_income = st.number_input('Median Income (in 10k USD)', min_value=0.0, value=8.3252)

# Preprocess input like training data
features = np.array([[longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
                      population, households, median_income]])

# Scale features
scaled_features = scaler.transform(features)

# Predict
price = model.predict(scaled_features)[0]

st.subheader(f"Predicted Median House Price: ${price * 100000:.2f}")

# Optional: Add explanations or charts
st.write("""
Note: Median House Price is predicted based on a linear regression model trained on California Housing dataset.
""")
