import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
print("Loaded API key:", repr(api_key))

def test_api_key():
    fetch_url = (
        "https://api.openweathermap.org/data/2.5/weather?q=Cleveland&appid=9e0bdf8447a0588d92e0dc93e031f0f1&units=imperial"
    )
    response = requests.get(fetch_url)
    data = response.json()
    print(data)


def fetch_weather(city):
    fetch_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=imperial"
    )
    response = requests.get(fetch_url)
    data = response.json()
    print(data)

if __name__ == "__main__":
    test_api_key()
