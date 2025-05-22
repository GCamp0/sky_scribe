# Handles generating quotes with Gemma
import ollama
def generate_quote(weather_info):
    prompt= f"""
Below is a weather report for {weather_info['city']}: and a personality. Id like you to generate a quote that matches the weather and personality. 

Do not repeat the weather report or any of the information in the weather report. just give me a quote that someone of that personality would say in that weather.

Do not put the quote in quotes or say anything other than the quote.
Weather data: {weather_info}
"""
    response = ollama.generate(
    model='gemma:2b',
    prompt=prompt,
    options={
        'temperature': 0.8
    },
    system=""
)
    return response["response"].strip()



if __name__ == "__main__":
    # Custom prompt logic just for this test
    test_weather = {
        "personality": "wizard",
        "Zip": "44032",
        "current_temp": 40,
        "condition": "windy and cold"
    }

    # You override the behavior here
    prompt = f"""
Below is a weather report for {test_weather['Zip']}: and a personality. Id like you to generate a quote that matches the weather and personality. 

Do not repeat the weather report or any of the information in the weather report. just give me a quote that someone of that personality would say in that weather.

Do not put the quote in quotes or say anything other than the quote.
Weather data: {test_weather}
"""

    response = ollama.generate(
        model="gemma:2b",
        prompt=prompt,
        options={"temperature": 0.9}
    )
    print("Test Quote:", response["response"].strip())