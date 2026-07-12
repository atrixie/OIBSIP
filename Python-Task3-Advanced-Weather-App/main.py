from PIL import Image, ImageTk
from io import BytesIO
import requests

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

from weather import get_weather
from forecast import get_forecast

root = tk.Tk()

root.title("Advanced Weather App")

root.geometry("900x1050")

root.configure(bg="#EAF4FF")

root.resizable(True, True)

title = tk.Label(
    root,
    text="🌦 Advanced Weather App",
    font=("Segoe UI", 22, "bold"),
    bg="#EAF4FF",
    fg="#1F3B73"
)

title.pack(pady=20)

search_frame = tk.Frame(root, bg="#EAF4FF")
search_frame.pack()

city_entry = ttk.Entry(
    search_frame,
    width=35,
    font=("Segoe UI", 12)
)

city_entry.grid(row=0, column=0, padx=10)

card = tk.Frame(
    root,
    bg="white",
    relief="ridge",
    bd=2
)

card.pack(
    padx=25,
    pady=20,
    fill="both",
    expand=True
)

card.pack_propagate(False)
card.config(height=700)

location_label = tk.Label(
    card,
    text="📍 Location",
    font=("Segoe UI", 18, "bold"),
    bg="white"
)

location_label.pack(pady=10)
icon_label = tk.Label(
    card,
    bg="white"
)

icon_label.pack(pady=5)

updated_label = tk.Label(
    card,
    text="Last Updated : --",
    font=("Segoe UI",11),
    bg="white",
    fg="gray"
)

updated_label.pack()

temp_label = tk.Label(
    card,
    text="🌡 Temperature : -- °C",
    font=("Segoe UI", 16),
    bg="white"
)

temp_label.pack()

feels_label = tk.Label(
    card,
    text="🤗 Feels Like : -- °C",
    font=("Segoe UI", 14),
    bg="white"
)

feels_label.pack()

weather_label = tk.Label(
    card,
    text="☁ Weather : --",
    font=("Segoe UI", 14),
    bg="white"
)

weather_label.pack()

desc_label = tk.Label(
    card,
    text="Description",
    font=("Segoe UI", 12),
    bg="white"
)

desc_label.pack()

humidity_label = tk.Label(
    card,
    text="💧 Humidity : -- %",
    font=("Segoe UI", 13),
    bg="white"
)

humidity_label.pack()

pressure_label = tk.Label(
    card,
    text="📈 Pressure : -- hPa",
    font=("Segoe UI", 13),
    bg="white"
)

pressure_label.pack()

wind_label = tk.Label(
    card,
    text="🌬 Wind Speed : -- m/s",
    font=("Segoe UI", 13),
    bg="white"
)

wind_label.pack()

visibility_label = tk.Label(
    card,
    text="👀 Visibility : -- km",
    font=("Segoe UI", 13),
    bg="white"
)

visibility_label.pack()

country_label = tk.Label(
    card,
    text="🌍 Country : --",
    font=("Segoe UI", 13),
    bg="white"
)

country_label.pack()

sunrise_label = tk.Label(
    card,
    text="🌅 Sunrise : --",
    font=("Segoe UI", 13),
    bg="white"
)

sunrise_label.pack()

sunset_label = tk.Label(
    card,
    text="🌇 Sunset : --",
    font=("Segoe UI", 13),
    bg="white"
)

sunset_label.pack()





def search_weather():
    

    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror(
            "Error",
            "Please enter a city."
        )
        return

    data = get_weather(city)

    if data is None:
        messagebox.showerror(
            "Error",
            "City not found or API Error."
        )
        return

    location_label.config(
    text=f"📍 {data['name']}, {data['sys']['country']}"
)

    temp_label.config(
        text=f"🌡 Temperature : {data['main']['temp']} °C"
    )

    feels_label.config(
        text=f"🤗 Feels Like : {data['main']['feels_like']} °C"
    )

    weather_label.config(
    text=f"☁ Weather : {data['weather'][0]['main'].title()}"
)

    desc_label.config(
        text=f"📝 {data['weather'][0]['description'].title()}"
    )

    humidity_label.config(
        text=f"💧 Humidity : {data['main']['humidity']} %"
    )

    pressure_label.config(
        text=f"📈 Pressure : {data['main']['pressure']} hPa"
    )

    wind_label.config(
        text=f"🌬 Wind Speed : {data['wind']['speed']} m/s"
    )

    visibility = data.get("visibility", 0) / 1000

    visibility_label.config(
        text=f"👀 Visibility : {visibility} km"
    )

    country_label.config(
        text=f"🌍 Country : {data['sys']['country']}"
    )
    icon = data["weather"][0]["icon"]

    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    try:
        image = requests.get(icon_url).content

        img = Image.open(BytesIO(image))

        photo = ImageTk.PhotoImage(img)

        icon_label.config(image=photo)
        icon_label.image = photo

    except Exception:
        pass

    updated_label.config(
        text=f"Last Updated : {datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
    )

    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"]
    ).strftime("%I:%M %p")

    sunset = datetime.fromtimestamp(
        data["sys"]["sunset"]
    ).strftime("%I:%M %p")

    sunrise_label.config(
        text=f"🌅 Sunrise : {sunrise}"
    )

    sunset_label.config(
        text=f"🌇 Sunset : {sunset}"
    )



    forecast = get_forecast(city)

    if forecast:

        forecast_window = tk.Toplevel(root)
        forecast_window.title("5-Day Forecast")
        forecast_window.geometry("650x450")

        box = ScrolledText(
            forecast_window,
            width=70,
            height=20,
            font=("Consolas", 11)
        )

        box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        box.insert(
            tk.END,
            f"{'Date':<15}{'Temp':<10}Weather\n"
        )

        box.insert(
            tk.END,
            "=" * 45 + "\n"
        )

        shown = set()

        for item in forecast["list"]:

            date = item["dt_txt"].split()[0]

            if date not in shown:

                shown.add(date)

                temp = round(item["main"]["temp"])

                weather = item["weather"][0]["description"].title()

                box.insert(
                    tk.END,
                    f"{date:<15}{str(temp)+'°C':<10}{weather}\n"
                )

            if len(shown) == 5:
                break

        box.config(state="disabled")


def clear():

    city_entry.delete(0, tk.END)

    location_label.config(text="📍 Location")

    temp_label.config(text="🌡 Temperature : -- °C")

    feels_label.config(text="🤗 Feels Like : -- °C")

    weather_label.config(text="☁ Weather : --")

    desc_label.config(text="Description")

    humidity_label.config(text="💧 Humidity : -- %")

    pressure_label.config(text="📈 Pressure : -- hPa")

    wind_label.config(text="🌬 Wind Speed : -- m/s")

    visibility_label.config(text="👀 Visibility : -- km")

    country_label.config(text="🌍 Country : --")

    sunrise_label.config(text="🌅 Sunrise : --")

    sunset_label.config(text="🌇 Sunset : --")

    updated_label.config(text="Last Updated : --")

    icon_label.config(image="")
    icon_label.image = None

    


button = ttk.Button(
    search_frame,
    text="Get Weather",
    command=search_weather
)

button.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)

clear_btn = ttk.Button(
    search_frame,
    text="Clear",
    command=clear
)

clear_btn.grid(
    row=0,
    column=2,
    padx=10,
    pady=5
)

city_entry.bind("<Return>", lambda event: search_weather())

root.mainloop()