# Weather API Script

## Overview
This Python script fetches real-time weather data for a specified city using the **WeatherAPI**. It provides current weather conditions and temperature in Celsius.

## Features
- Retrieves live weather information.
- Displays weather condition and temperature.
- Handles invalid city inputs gracefully.

## Requirements
- Python 3.x
- `requests` module (install with `pip install requests`)
- A valid API key from [WeatherAPI](https://www.weatherapi.com/)

## How It Works
1. The user enters a city name.
2. The script sends a request to WeatherAPI to fetch current weather data.
3. The response is processed to extract and display:
   - Weather condition (e.g., "Sunny", "Cloudy").
   - Temperature in Celsius.
4. If the city name is incorrect, an error message is displayed.

## Code Explanation

### API Configuration
```python
API_KEY = "your_api_key"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
```
- Replace `your_api_key` with a valid WeatherAPI key.
- `BASE_URL` is the endpoint for retrieving current weather data.

### Fetching Weather Data
```python
def get_weather(city):
    URL = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(URL)
```
- Constructs the API URL dynamically with the city name.
- Sends an HTTP GET request to fetch weather details.

### Handling API Response
```python
if response.status_code == 200:
    data = response.json()
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    print(f"\U0001F324 Weather in {city}: {weather}, {temperature}°C")
else:
    print("\u274C City not found. Please try again.")
```
- Extracts weather condition and temperature from the API response.
- If the request fails, an error message is shown.

### User Input
```python
city = input("Enter a city: ")
get_weather(city)
```
- Prompts the user to enter a city name.
- Calls `get_weather()` function to retrieve and display the weather.

## How to Run
1. Save the script as `weather.py`.
2. Run the script using:
   ```sh
   python weather.py
   ```
3. Enter a city name when prompted.

## Example Output
```
Enter a city: New York
🌤 Weather in New York: Sunny, 22°C
```

## Future Enhancements
- Add support for temperature in Fahrenheit.
- Include additional data like humidity and wind speed.
- Implement a graphical interface (GUI) using Tkinter or PyQt.

## Notes
- Ensure you replace `API_KEY` with your valid WeatherAPI key.
- Internet connection is required for API requests.

---

This script is a simple yet effective way to fetch live weather data using Python!

