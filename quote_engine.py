import os
import sys
import httpx
import ollama

# Set the correct cert path for secure requests (works in .app and dev mode)
if getattr(sys, 'frozen', False):
    base_path = os.path.join(os.path.dirname(sys.executable), "..", "Resources")
else:
    base_path = os.path.dirname(__file__)

cert_path = os.path.join(base_path, "cert", "cacert.pem")
os.environ["SSL_CERT_FILE"] = cert_path

# Generates a personality-based quote about the weather using Ollama
def generate_quote(weather_info):
    try:
        httpx.get("http://localhost:11434", timeout=1)
    except Exception:
        return "Ollama is not running. Please start Ollama before using Sky Scribe."

    # Improved AI prompt with clearer instruction and tone control
    prompt = f"""
You are an AI tasked with writing a brief, expressive quote that reflects how a person with a given personality might react to today's weather.

Instructions:
- Respond as if you *are* that personality type.
- Do not repeat weather facts directly (e.g., "It's 75°F and sunny").
- Do not reference 'the weather report' or act like a narrator unleess specified.
- Do not include quotation marks or attribution (no "John said...").
- Make it sound natural and fitting for that personality.

Context:
Personality: {weather_info.get('personality', 'neutral')}
Location: {weather_info.get('city', 'your area')}
Weather Data: {weather_info}

Now write the quote.
"""

    response = ollama.generate(
        model="gemma:2b",
        prompt=prompt,
        options={"temperature": 0.8},
        system=""
    )

    return response["response"].strip()

# Standalone test mode
if __name__ == "__main__":
    print("Using cert from:", cert_path)
    print("Cert file exists:", os.path.exists(cert_path))

    test_weather = {
        "personality": "philosopher",
        "city": "Cleveland",
        "current_temp": 40,
        "condition": "windy and cold"
    }

    print("Sample output:\n", generate_quote(test_weather))
