from quote_engine import generate_quote
from weather_api import fetch_weather
import subprocess

def show_notification(weather_info,quote):
    # This function actually creates the notification using the data created in main()
    message = (
    f"{quote}\n\n"
    f"{weather_info['condition'].title()} | {round(weather_info['current_temp'])}°F\n\n"
    f"High: {round(weather_info['temp_max'])}°F\n"
    f"Low: {round(weather_info['temp_min'])}°F\n\n"
    )

    # Escape quotes in message
    safe_message = message.replace('"', "'")

    # Build and run the AppleScript command
    script = f'display notification "{safe_message}" with title "Sky Scribe"'
    subprocess.run(["osascript", "-e", script])

    

def main():
    #inputs to the program from the user
    city = input("Enter a city: ").strip()
    personality = input("Give a one word personality: ").strip()
    
    #fetch the weather data from the API and append the personality to the weather data
    weather_info = fetch_weather(city)
    weather_info["personality"] = personality
    
    #receive the quote from Gemma
    quote = generate_quote(weather_info)
    
    #prints
    print (weather_info) # 👈 shows the weather
    print (quote) # 👈 shows the AI’s response
   
    #shows the notification
    show_notification(weather_info, quote)



#
if __name__ == "__main__":
    main()
