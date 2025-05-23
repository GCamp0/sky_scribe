import schedule
import time
import json
from quote_engine import generate_quote
from weather_api import fetch_weather
from main import show_notification

# Load config.json
with open("config.json", "r") as file:
    config = json.load(file)

notify_times = config.get("Notify_Times", ["08:00"])
Zip = config.get("Zip", "44032")
personality = config.get("Personality", "Poetic")
api_key = config.get("Api_Key")

def run_sky_scribe():
    weather_info = fetch_weather(Zip, api_key)
    weather_info["personality"] = personality
    quote = generate_quote(weather_info)
    show_notification(weather_info, quote)

for t in notify_times:
    schedule.every().day.at(t).do(run_sky_scribe)

print("Sky Scribe scheduler running for:", notify_times)

while True:
    schedule.run_pending()
    time.sleep(60)
