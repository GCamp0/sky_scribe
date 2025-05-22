# Sky Scribe

Sky Scribe is a personal project I built to sharpen my Python skills while creating something functional and focused on user experience. It's a macOS desktop app that combines real-time weather data and AI to generate quotes tailored to both the weather and the user's chosen personality. These quotes are then displayed as native macOS notifications on a schedule or on demand.

The project taught me how to structure an application, build a user-friendly GUI, and handle cross-platform quirks like macOS's UI limitations. I also learned how to work with background schedulers, config files, and local AI models. The result is a real, usable desktop tool that feels cohesive and complete.

This wasn't just about writing code — it was about designing something that feels polished from end to end. I encountered and solved a number of problems you'd run into in real-world software:
- We hit layout limitations in Tkinter, and I had to learn how to use the grid system precisely to get a clean, centered layout.
- macOS doesn’t honor custom button colors in Tkinter, so I had to ditch native buttons and recreate them using `Canvas` objects to control how they looked and responded.
- Scheduling logic had to balance between accurate timing and low CPU usage, so we configured the `schedule` loop to sleep intelligently.
- I wanted the app to feel responsive, so I implemented a file watcher that auto-restarts the background scheduler when the user updates settings in the GUI.
- To keep things clean for users, I swapped out city name input for ZIP code support, and made sure all data was validated and handled smoothly.

Every one of those steps pushed me to debug, refactor, and rethink how each piece fits together. It wasn't always obvious what was broken — sometimes we had to step back, restructure, or start over with a new approach. But that’s part of the job, and I pushed through every roadblock until the pieces clicked.

## Features
- Daily notifications with AI-generated weather quotes
- Configurable ZIP code and personality-based prompts
- Multi-time daily scheduling (comma-separated entry)
- "Do Now" button to manually trigger a quote
- Live config watcher that auto-restarts the scheduler when the config is changed
- Custom dark-themed GUI built with Tkinter
- Logo placement and canvas-based buttons to ensure proper rendering on macOS

## My Role
- Designed the architecture and planned how components should connect
- Wrote the weather fetch logic, API integration, and AI quote generation logic
- Developed the GUI layout and styling, iterating multiple times for a clean, professional feel
- Solved macOS-specific issues with button rendering using canvas-based custom buttons
- Built the config system and ensured compatibility between GUI, scheduler, and watcher
- Added support for multiple notification times and switched from city-based to ZIP-based weather fetching
- Guided the use of AI assistance (ChatGPT) to help generate cleaner code and explore design options, but handled debugging, final implementation, and all project decisions myself

## AI’s Role
I used ChatGPT during development as a coding assistant. It helped me speed up implementation, suggested fixes when I was stuck, and provided code snippets to build from. I always reviewed, edited, and integrated everything manually. This app is mine — AI was a tool, not a co-pilot.

## Why It Matters
This project shows that I can take an idea, break it into systems, and follow through to execution. I didn’t just build something that works — I made something that looks and feels like a finished product. It challenged me to understand real development concerns like file structure, modularity, visual design, and user flow. I approached this like a professional, and the final product reflects that. The lessons I learned building Sky Scribe — especially around user input handling, UI responsiveness, and system integration — will carry forward into every other project I build.

## Requirements
- Python 3.9+
- Pillow (for image handling)
- requests (for OpenWeatherMap API calls)
- schedule (for timing notifications)
- watchdog (for monitoring file changes)
- ollama (for local AI quote generation)

To install dependencies:
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install manually:
```bash
pip install requests schedule watchdog pillow
```

---

Sky Scribe is still evolving. Next steps include consolidating everything into a unified `app.py`, adding quote history logging, and eventually packaging the entire thing as a standalone `.app` for macOS with a custom icon and launch behavior.
This is my first independant python project so let me know if you have any advice. 
Thanks.
