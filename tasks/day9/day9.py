import requests

API_KEY = "e873af13a9cd4a65bb0143519251503"  # Your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    URL = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        weather = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        print(f"🌤 Weather in {city}: {weather}, {temperature}°C")
    else:
        print("❌ City not found. Please try again.")

# User Input
city = input("Enter a city: ")
get_weather(city)

