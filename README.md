# Sky Scribe: AI-Powered Weather Notification App

Sky Scribe is a Python desktop assistant I built that combines live weather data with AI-generated quotes. The idea was to create something that runs daily and gives me a little bit of poetic motivation based on the weather in my area.

---

## What It Does
- Pulls weather data for a set city using the OpenWeatherMap API
- Sends the weather details and a chosen personality to a locally hosted AI model using Ollama (I use Gemma)
- Generates a quote based on that mood and weather
- Displays the result as a native macOS notification
- Runs every day at a set time (like 8:00 AM), with support for future time slots
- Automatically restarts if I change the config file

---

## My Role
I came up with this idea while brainstorming Python portfolio projects. While I used ChatGPT 4o as a tutor and to help fill in the gaps I made sure to understand each piece of code asking questions where I needed to. 

I asked questions to make sure I understood why things were being done a certain way, especially around watchdog, the scheduler, and config system. I also pointed out when code suggestions were wrong or missing something, and I pushed for cleaner architecture and control flow. 

One example was when I realized importing `main.py` would trigger unwanted input prompts — so I pushed to only import the necessary functions. I also questioned why we’d use JSON if we were eventually building a UI, and that helped shape the app's direction.

---

## What I needed help for
I used ChatGPT to help figure out a solid structure for the project and which packages to use and how to utilize them. It helped guide me through:
- Using the `schedule` library to run tasks at specific times
- Setting up `watchdog` to monitor changes to `config.json`
- Restarting the scheduler subprocess when the config file updates
- Using `subprocess.Popen()` and `terminate()` properly

That said, I was the one who put it all together, made it work end-to-end, and fixed any bad assumptions or broken logic.

---

## What I Learned
- How to build scheduled Python scripts that run cleanly in the background
- How to structure modular Python apps across multiple files
- How to monitor files and restart processes using `watchdog`
- Why you use `subprocess.Popen()` instead of trying to import and rerun a file
- How to write readable, testable, and reusable code
- How to track and manage changes with Git and GitHub

---

## File Breakdown
- `main.py` – manually runs a single quote cycle using user input
- `scheduler.py` – runs automatically based on times set in `config.json`
- `config_watcher.py` – watches for updates to the config and restarts the scheduler
- `quote_engine.py` – builds and sends the prompt to the AI model
- `weather_api.py` – gets and formats weather data from OpenWeatherMap
- `config.json` – lets you set times, city, and personality for scheduled use 
- `.env` – stores the API key securely (not included in GitHub)
- `requirements.txt` – all the packages I used

---

## How To Run
1. Clone the repo
2. Add your API key to a `.env` file:
```bash
OPENWEATHER_API_KEY=your_key_here
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set your city, mood, and times in `config.json`
5. Run the config watcher:
```bash
python3 config_watcher.py
```
You’ll get a daily motivational weather update right on your desktop.

---

## What’s Next
- Adding a UI so you don’t have to edit `config.json` manually
- Making it work on Windows and Linux too
- Storing past quotes to a local file or log
- Packaging it as a full `.app` for macOS using the custom icon I built

---

Sky Scribe started as a side project to help me get better at Python, and it’s already taught me more than a course could’ve. There’s still more I want to do with it, but I’m proud of what I’ve built so far.
