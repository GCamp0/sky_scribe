from quote_engine import generate_quote
from weather_api import fetch_weather

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



#
if __name__ == "__main__":
    main()
