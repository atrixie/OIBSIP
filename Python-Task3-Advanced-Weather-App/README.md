# 🌦️ Advanced Weather App

A modern Python-based Weather Application built using **Tkinter** and the **OpenWeather API**. The application provides real-time weather information along with a 5-day weather forecast through a clean and user-friendly graphical interface.

---

## 📌 Features

- 🌍 Search weather by city name
- 🌡️ Real-time temperature
- 🤗 Feels Like temperature
- ☁️ Weather condition
- 📝 Detailed weather description
- 💧 Humidity
- 🌬️ Wind Speed
- 📈 Atmospheric Pressure
- 👀 Visibility
- 🌅 Sunrise Time
- 🌇 Sunset Time
- 🕒 Last Updated timestamp
- 🖼️ Dynamic Weather Icons
- 📅 5-Day Weather Forecast (Popup Window)
- 🧹 Clear Button to reset data
- ⚠️ Error handling for invalid city names and API issues

---

## 🛠️ Tech Stack

- Python 3
- Tkinter
- OpenWeather API
- Requests
- Pillow
- Python Dotenv

---

## 📂 Project Structure

```
Python-Task3-Advanced-Weather-App/
│
├── main.py
├── weather.py
├── forecast.py
├── .env.example
├── requirements.txt
├── README.md
└── screenshots/
    ├── home.png
    ├── weather-result.png
    └── forecast.png
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/atrixie/OIBSIP.git
```

### Navigate to the project

```bash
cd Python-Task3-Advanced-Weather-App
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file inside the project folder.

```env
API_KEY=YOUR_OPENWEATHER_API_KEY
```

You can get a free API key from:

https://openweathermap.org/api

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📸 Screenshots

### 🏠 Home Screen

![Home](screenshots/home.png)

---

### 🌦️ Weather Information

![Weather](screenshots/weather-result.png)

---

### 📅 5-Day Forecast

![Forecast](screenshots/forecast.png)

---

## 📚 Concepts Used

- GUI Programming with Tkinter
- REST API Integration
- JSON Parsing
- Environment Variables
- Exception Handling
- Modular Programming
- Image Processing
- Event Handling

---

## 🎯 Future Improvements

- 📍 Detect Current Location Automatically
- 🌙 Dark Mode
- 🌡️ Celsius / Fahrenheit Toggle
- ⭐ Favorite Cities
- 📊 Weather History
- 📈 Graphical Weather Trends

---

## 📄 License

This project is created for learning purposes as part of the **Oasis Infobyte Python Programming Internship**.

---

## 👨‍💻 Author

**Nikijon Kakati**

- GitHub: https://github.com/atrixie
- LinkedIn: https://www.linkedin.com/in/nikijon-kakati-076a3337a/

⭐ If you found this project helpful, consider giving it a star!