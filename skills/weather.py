import os
import requests

from dotenv import load_dotenv
from modules.speech import speak

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ==========================================
# Weather Function
# ==========================================

def get_weather(city):

    if not API_KEY:
        speak("Weather API key is missing. Please check your environment file.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:

            message = data.get("message", "Unable to fetch weather.")

            speak(f"Sorry. {message.capitalize()}.")

            return

        # ===============================
        # Extract Weather Details
        # ===============================

        city_name = data["name"]
        country = data["sys"]["country"]

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        wind_speed = data["wind"]["speed"]

        description = data["weather"][0]["description"].title()

        visibility = data.get("visibility", 0) / 1000

        # ===============================
        # Speak Result
        # ===============================

        speak(
            f"Here's the live weather report for {city_name}, {country}. "
            f"Currently, the weather is {description}. "
            f"The temperature is {temperature:.1f} degrees Celsius, "
            f"but it feels like {feels_like:.1f} degrees. "
            f"The humidity is {humidity} percent. "
            f"Atmospheric pressure is {pressure} hectopascals. "
            f"The wind speed is {wind_speed:.1f} meters per second. "
            f"Visibility is approximately {visibility:.1f} kilometers."
        )

    except requests.exceptions.Timeout:

        speak("The weather service took too long to respond. Please try again.")

    except requests.exceptions.ConnectionError:

        speak("I couldn't connect to the weather service. Please check your internet connection.")

    except Exception as e:

        print("Weather Error:", e)

        speak("Sorry, something went wrong while fetching the weather.")