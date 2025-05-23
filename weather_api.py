import requests

# Fetch current weather data from OpenWeatherMap
def fetch_weather(zip_code, api_key):
    if not api_key or api_key == "your_api_key_here":
        raise ValueError("Missing or placeholder API key. Please enter a valid one.")

    fetch_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?zip={zip_code},us&appid={api_key}&units=imperial"
    )

    response = requests.get(fetch_url)
    data = response.json()

    if response.status_code != 200:
        raise ValueError(data.get("message", "Unknown API error"))

    return {
        "city": data["name"],
        "current_temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "condition": data["weather"][0]["description"]
    }

# Optional dev test mode (disabled until key is passed in)
if __name__ == "__main__":
    raise RuntimeError("Direct test mode requires a valid API key to be passed manually.")
