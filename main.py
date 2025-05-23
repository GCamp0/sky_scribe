import os
import sys

if getattr(sys, 'frozen', False):
    # This gets path like: .../app.app/Contents/MacOS/
    base_path = os.path.dirname(sys.executable)
    # Go to: .../app.app/Contents/Resources/cert/cacert.pem
    cert_path = os.path.join(base_path, '..', 'Resources', 'cert', 'cacert.pem')
    cert_path = os.path.abspath(cert_path)
    os.environ['SSL_CERT_FILE'] = cert_path

from config_editor import launch_gui
from weather_api import fetch_weather
from quote_engine import generate_quote
from notifier import show_notification  # moved here

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
    cert_path = os.path.join(base_path, 'cert', 'cacert.pem')
    os.environ["SSL_CERT_FILE"] = cert_path

def main():
    zip_code = input("Enter a ZIP code: ").strip()
    personality = input("Enter a one-word personality: ").strip()

    weather_info = fetch_weather(zip_code)
    weather_info["personality"] = personality

    quote = generate_quote(weather_info)

    print(weather_info)
    print(quote)

    show_notification(weather_info, quote)

if __name__ == "__main__":
    main()
