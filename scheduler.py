import schedule
import time
import json
from quote_engine import generate_quote
from weather_api import fetch_weather
from main import show_notification

# Load config.json
with open("config.json", "r") as file:
    config = json.load(file)

notify_times = config.get("notify_times", [])
city = config.get("default_city", "Cleveland")
personality = config.get("default_personality", "calm")

def run_sky_scribe():
    weather_info = fetch_weather(city)
    weather_info["personality"] = personality
    quote = generate_quote(weather_info)
    show_notification(weather_info, quote)

for t in notify_times:
    schedule.every().day.at(t).do(run_sky_scribe)

while True:
    schedule.run_pending()
    time.sleep(60)
