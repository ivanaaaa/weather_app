import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your OpenWeatherMap API key
API_KEY = "d5a21bdced1b5e7ebade55c0a9073c82"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "Unknown error"))
            return

        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()

        result_label.config(
            text=f"Weather in {city_name}\n"
                 f"Temperature: {temperature}°C\n"
                 f"Condition: {description}",
            fg="white"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create Tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")
root.configure(bg="#1e1e2f")

# Center window on screen
window_width = 350
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Title label
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 16, "bold"), bg="#1e1e2f", fg="white")
title_label.pack(pady=10)

# City input
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=5)

# Button to get weather
get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#4CAF50", fg="white")
get_button.pack(pady=5)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 13), bg="#1e1e2f", fg="white", justify="center")
result_label.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
