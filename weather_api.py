import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
print("Loaded API key:", repr(api_key))

# Just a function to test if the API key is working
def test_api_key():
    fetch_url = (
    f"https://api.openweathermap.org/data/2.5/weather?q=Cleveland&appid={api_key}&units=imperial"
    )
    response = requests.get(fetch_url)
    data = response.json()
    print(data)

#collect weather data from the API
#TODO: add error handling for invalid data returns
def fetch_weather(Zip):
    fetch_url = (
    f"https://api.openweathermap.org/data/2.5/weather?zip={Zip},us&appid={api_key}&units=imperial"
    )

    response = requests.get(fetch_url)
    data = response.json()
    print(data)
    weather_info = {
        "city": data["name"],
        "current_temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "condition": data["weather"][0]["description"] 
    }
    return (weather_info)




if __name__ == "__main__":
    test_api_key()
