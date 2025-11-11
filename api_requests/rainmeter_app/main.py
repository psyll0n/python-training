import os
import requests
import json
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# OpenWeatherMap API endpoint
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Retrieve sensitive information from environment variables
API_KEY = os.getenv("OWM_API_KEY")  # OpenWeatherMap API key
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio Account SID
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")  # Twilio Auth Token
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Twilio phone number
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")  # Recipient phone number

# Location coordinates (latitude and longitude)
LATITUDE = 45.327065
LONGITUDE = 14.442176

# Weather API request parameters
weather_params = {
    "appid": API_KEY,
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "cnt": 4,  # Number of forecast intervals to retrieve
}

try:
    # Make a request to the OpenWeatherMap API
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the JSON response
    weather_data = response.json()

    # Check if it will rain in the next few hours
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if condition_code < 700:  # Weather condition codes below 700 indicate rain
            will_rain = True
            break

    if will_rain:
        # Initialize the Twilio client
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        # Send a message using Twilio
        message = client.messages.create(
            body="It will rain in the next few hours. Bring an umbrella! ☔️",
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER,
        )
        print(f"Message sent! Status: {message.status}")
    else:
        print("No rain expected in the next few hours.")

except requests.exceptions.RequestException as e:
    print(f"Error with the weather API request: {e}")
except json.JSONDecodeError:
    print("Response content is not valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
