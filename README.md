# 🚀 Pak AstroAI – Climate & Pollution Tracker

## 🌍 NASA Space Apps Challenge 2025

A real-time weather and air quality monitoring application designed specifically for Pakistan. Track climate conditions, air pollution levels, and weather forecasts for any Pakistani city.

![Pak AstroAI Banner](https://img.shields.io/badge/NASA%20Space%20Apps-2025-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Flask](https://img.shields.io/badge/Flask-2.3.2-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🌡️ **Real-time Weather Data** - Current temperature, humidity, wind speed, and conditions
- 💨 **Air Quality Index (AQI)** - Live pollution levels including PM2.5, PM10, NO2, CO
- 📅 **7-Day Weather Forecast** - Extended weather outlook for better planning
- 📍 **Geolocation Support** - Automatic detection of user's location
- ⚖️ **City Comparison** - Compare air quality between different Pakistani cities
- 🤖 **AI Assistant Chatbot** - Get instant environmental safety tips
- 🎨 **Dynamic UI** - Weather-responsive backgrounds and modern neon theme
- 📱 **Fully Responsive** - Works perfectly on mobile, tablet, and desktop

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Backend:** Flask (Python)
- **APIs:**
  - OpenWeatherMap API - Weather & forecast data
  - AirVisual API - Air quality data
- **Deployment:** Render / Streamlit Cloud

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pak-astroai.git
cd pak-astroai
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env file and add your API keys
# OPENWEATHER_API_KEY=your_key_here
# AIRVISUAL_API_KEY=your_key_here
```

**Note:** The provided API keys in the code are for demo purposes. Get your own keys at:
- OpenWeatherMap: https://openweathermap.org/api
- AirVisual: https://www.iqair.com/air-pollution-data-api

### 5. Create required folders

```bash
mkdir templates static
```

### 6. Move files to correct locations

- Save the HTML file as `templates/index.html`
- Save the Python file as `app.py`

### 7. Run the application

```bash
python app.py
```

### 8. Open in browser

Navigate to `http://localhost:5000` in your web browser

## 📁 Project Structure

```
pak-astroai/
├── app.py                 # Flask backend server
├── templates/
│   └── index.html        # Main HTML template
├── static/               # Static assets (optional)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create from .env.example)
├── .env.example          # Example environment file
├── README.md            # Documentation
└── Procfile             # Deployment configuration
```

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/api/weather/<city>` | GET | Get weather data for a city |
| `/api/air-quality/<city>` | GET | Get AQI data for a city |
| `/api/forecast/<city>` | GET | Get 7-day forecast |
| `/api/compare` | POST | Compare two cities |
| `/api/location` | POST | Get data by coordinates |
| `/api/chatbot` | POST | Chat with AI assistant |

## 🚀 Deployment

### Deploy to Render

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Push to GitHub
3. Connect to Render
4. Add environment variables
5. Deploy!

### Deploy to Streamlit Cloud

For Streamlit version (alternative):
1. Convert Flask app to Streamlit
2. Push to GitHub
3. Deploy via Streamlit Cloud

## 🎯 Key Features Explained

### Air Quality Index (AQI) Levels
- **0-50 (Good):** Air quality is satisfactory ✅
- **51-100 (Moderate):** Acceptable for most people ⚠️
- **101-150 (Unhealthy for Sensitive Groups):** Sensitive groups may experience health effects 🟡
- **151-200 (Unhealthy):** Everyone may experience health effects 🟠
- **201-300 (Very Unhealthy):** Health warnings of emergency conditions 🔴
- **300+ (Hazardous):** Emergency conditions affecting entire population 🟣

### Smart Recommendations
The app provides real-time health recommendations based on current AQI levels:
- Mask wearing guidelines
- Exercise safety tips
- Outdoor activity suggestions
- Vulnerable group warnings

## 👥 Team Pak AstroAI

Built with ❤️ for NASA Space Apps Challenge 2025

## 📄 License

MIT License - feel free to use this project for your own purposes!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🙏 Acknowledgments

- NASA Space Apps Challenge for the opportunity
- OpenWeatherMap for weather data API
- AirVisual for air quality data API
- The people of Pakistan who inspire us to build solutions for cleaner air

---

**Remember:** Clean air is a human right. Let's work together for a pollution-free Pakistan! 🌍💚