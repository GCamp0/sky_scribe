#app for editing the config.json file also user friendly
import tkinter as tk # for the GUI
from tkinter import messagebox # for the message box
import json # for saving the config
import os #might use this for checking if the config file exists
import subprocess # for running the watcher
from quote_engine import generate_quote # for generating the quote for now button
from weather_api import fetch_weather # for fetching the weather data
from main import show_notification # for showing the notification
from PIL import ImageTk, Image # for the icon

# Check if config.json exists, if not create it with default values
scheduler_process = subprocess.Popen(["python3", "scheduler.py"])


#function for save button which updates the config.json file
# and saves the user input
def save_settings():
    Zip = zip_entry.get()
    Personality = personality_entry.get()
    raw_times = time_entry.get()
    
    notify_times = [
        t.strip()
        for t in raw_times.split(",")
     if t.strip() and len(t.strip()) == 5 and ":" in t
    ]


    new_config = {
        "Zip": Zip,
        "Personality": Personality,
        "Notify_Times": notify_times
    }

    with open("config.json", "w") as f:
        json.dump(new_config, f, indent=4)

    # Restart the scheduler process
    global scheduler_process
    scheduler_process.terminate()
    scheduler_process = subprocess.Popen(["python3", "scheduler.py"])

    # Show a message box to confirm the settings were saved
    messagebox.showinfo("Saved", "Settings were saved successfully.")

#function for the "Do Now" button which runs the programs with current text boxes
def run_now():
    Zip = zip_entry.get()
    Personality = personality_entry.get()

    weather_info = fetch_weather(Zip)
    weather_info["Personality"] = Personality  # Match your capitalized keys

    quote = generate_quote(weather_info)
    show_notification(weather_info, quote)


# Root window setup
root = tk.Tk()
root.title("Sky Scribe")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Fonts and colors
label_font = ("Helvetica", 11)
entry_font = ("Helvetica", 11)
bg_color = "#1e1e1e"
fg_color = "white"

# Logo
logo_image = Image.open("sky_logo.png")
logo_image = logo_image.resize((48, 48))
logo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo, bg=bg_color)
logo_label.image = logo
logo_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")

# Title
title_label = tk.Label(root, text="Sky Scribe", font=("Helvetica", 18, "bold"), bg=bg_color, fg=fg_color)
title_label.grid(row=0, column=1, padx=5, pady=10, sticky="w")

# Zip Code
tk.Label(root, text="Zip Code:", font=label_font, bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")
zip_entry = tk.Entry(root, font=entry_font)
zip_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")

# Personality
tk.Label(root, text="Personality:", font=label_font, bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")
personality_entry = tk.Entry(root, font=entry_font)
personality_entry.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="ew")

# Notify Times
tk.Label(root, text="Notify Times (comma-separated):", font=label_font, bg=bg_color, fg=fg_color).grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")
time_entry = tk.Entry(root, font=entry_font)
time_entry.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="ew")

# Button frame
button_frame = tk.Frame(root, bg=bg_color)
button_frame.grid(row=4, column=0, columnspan=2, pady=15)

def on_save_click(event=None):
    save_settings()

save_canvas = tk.Canvas(button_frame, width=100, height=30, bg="#444", highlightthickness=0)
save_canvas.create_text(50, 15, text="Save", fill="white", font=("Helvetica", 11))
save_canvas.bind("<Button-1>", on_save_click)
save_canvas.pack(side="left", padx=10)


def on_now_click(event=None):
    run_now()

now_canvas = tk.Canvas(button_frame, width=100, height=30, bg="#444", highlightthickness=0)
now_canvas.create_text(50, 15, text="Do Now", fill="white", font=("Helvetica", 11))
now_canvas.bind("<Button-1>", on_now_click)
now_canvas.pack(side="right", padx=10)


# Allow input fields to stretch
root.grid_columnconfigure(1, weight=1)

# Start GUI loop
root.mainloop()



