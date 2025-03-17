import requests

def fetch_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()["value"]
        print("\n Random Joke:\n", joke)
    else:
        print("Failed to fetch joke.")

def fetch_weather(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    
    if response.status_code == 200 and "results" in response.json():
        data = response.json()["results"][0]
        lat, lon = data["latitude"], data["longitude"]
        
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weathercode"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()["current"]
            temp = weather_data["temperature_2m"]
            print(f"\n Weather in {city}:\nTemperature: {temp}°C")
        else:
            print("Failed to fetch weather.")
    else:
        print("City not found.")

def weather_cli():
    city = input("Enter your city: ")
    fetch_weather(city)

if __name__ == "__main__":
    fetch_random_joke()
    weather_cli()
