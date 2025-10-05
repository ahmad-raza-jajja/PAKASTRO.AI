from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 🔑 API Keys (تمہاری اصل keys یہاں شامل ہیں)
OPENWEATHER_API_KEY = "5e65db8fb32a8b7cf252147fc3e47bc9"
AIRVISUAL_API_KEY = "d819389d-a6af-4019-a620-5370975f3bba"

@app.route('/')
def index():
    """Render the main application page"""
    return render_template('index.html')

@app.route('/api/weather/<city>')
def get_weather(city):
    """Get weather data for a specific city"""
    try:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},PK&appid={OPENWEATHER_API_KEY}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if weather_response.status_code != 200:
            return jsonify({"error": "City not found"}), 404

        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/air-quality/<city>')
def get_air_quality(city):
    """Get air quality data for a specific city"""
    try:
        airvisual_url = f"https://api.airvisual.com/v2/city?city={city}&state=Punjab&country=Pakistan&key={AIRVISUAL_API_KEY}"
        response = requests.get(airvisual_url)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data['data'])
        else:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},PK&appid={OPENWEATHER_API_KEY}"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            if 'coord' in weather_data:
                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                pollution_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
                pollution_response = requests.get(pollution_url)
                pollution_data = pollution_response.json()

                if 'list' in pollution_data and len(pollution_data['list']) > 0:
                    aqi_data = pollution_data['list'][0]
                    return jsonify({
                        'current': {
                            'pollution': {
                                'aqius': aqi_data['main']['aqi'] * 50,
                                'mainus': 'p2',
                                'ts': datetime.now().isoformat()
                            }
                        },
                        'pollution': {
                            'p2': {'v': aqi_data['components'].get('pm2_5', 0)},
                            'p1': {'v': aqi_data['components'].get('pm10', 0)},
                            'n2': {'v': aqi_data['components'].get('no2', 0)},
                            'co': {'v': aqi_data['components'].get('co', 0) / 1000}
                        }
                    })
            return jsonify({"error": "Air quality data not available"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/forecast/<city>')
def get_forecast(city):
    """Get 7-day weather forecast for a specific city"""
    try:
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city},PK&appid={OPENWEATHER_API_KEY}&units=metric&cnt=40"
        response = requests.get(forecast_url)

        if response.status_code != 200:
            return jsonify({"error": "Forecast not found"}), 404

        data = response.json()
        daily_forecasts = {}
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            if date not in daily_forecasts:
                daily_forecasts[date] = {
                    'date': date,
                    'temp_max': item['main']['temp_max'],
                    'temp_min': item['main']['temp_min'],
                    'weather': item['weather'][0]['main'],
                    'icon': item['weather'][0]['icon']
                }
            else:
                daily_forecasts[date]['temp_max'] = max(daily_forecasts[date]['temp_max'], item['main']['temp_max'])
                daily_forecasts[date]['temp_min'] = min(daily_forecasts[date]['temp_min'], item['main']['temp_min'])

        forecast_list = list(daily_forecasts.values())[:7]
        return jsonify({"list": forecast_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    """Simple chatbot for environmental tips"""
    try:
        data = request.json
        message = data.get('message', '').lower()

        responses = {
            'aqi': 'AQI (Air Quality Index) measures air pollution levels. 0-50 is Good, 51-100 is Moderate, etc.',
            'mask': 'When AQI > 100, wear an N95 mask outdoors.',
            'pollution': 'Main pollutants include PM2.5, PM10, NO2, CO, O3, and SO2.',
            'health': 'Air pollution can cause respiratory and heart issues.',
            'tips': 'Tips: Check AQI daily, use air purifiers, close windows on bad days, wear masks outdoors.',
            'weather': 'Weather affects air quality. Rain clears pollutants; still air traps them.',
            'default': "Ask about AQI, masks, pollution, or health effects!"
        }

        response = responses['default']
        for key in responses:
            if key in message:
                response = responses[key]
                break

        return jsonify({'response': response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

