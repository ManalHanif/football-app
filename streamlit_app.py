import streamlit as st
import requests

# FastAPI URL (deployed on Render)
FASTAPI_URL = "https://football-app-4ils.onrender.com/predict"

# Streamlit interface to take inputs
st.title("Football Player Prediction")

st.header("Enter Player Features")

# Collect input values
highest_value = st.number_input("Highest Value", min_value=0, max_value=100000000, value=1000000)
appearance = st.number_input("Appearance", min_value=0, max_value=1000, value=10)
minutes_played = st.number_input("Minutes Played", min_value=0, max_value=10000, value=500)
award = st.number_input("Award", min_value=0, max_value=50, value=1)
assists = st.number_input("Assists", min_value=0.0, max_value=100.0, value=5.0)
goals = st.number_input("Goals", min_value=0.0, max_value=100.0, value=10.0)
games_injured = st.number_input("Games Injured", min_value=0, max_value=50, value=2)

# Collect the input data into a dictionary
input_data = {
    "highest_value": highest_value,
    "appearance": appearance,
    "minutes_played": minutes_played,
    "award": award,
    "assists": assists,
    "goals": goals,
    "games_injured": games_injured,
}

# Button to trigger prediction
if st.button("Get Prediction"):
    try:
        # Send the input data to FastAPI (POST request)
        response = requests.post(FASTAPI_URL, json=input_data)
        
        if response.status_code == 200:
            prediction = response.json()
            # Display the prediction result
            st.success(f"Prediction: {prediction['pred']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

