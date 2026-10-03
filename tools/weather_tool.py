import requests
from tools.map_tool import get_coordinates


def get_weather(city):
    """
    Fetch weather information for a city
    """

    coords = get_coordinates(city)

    if not coords:
        
        return f"❌ Could not find location for {city}"

    lon, lat = coords

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,weather_code"
    }

    response = requests.get(url, params=params)

    # debug statement to print the response
    print("Weather API response status code:", response.status_code)

    data = response.json()
    print("Weather API response data:", data)  # Debugging line to print the entire response
    # print("Weather API response:", data)
    current = data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    weather_code = current["weather_code"]

    weather_description = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
    }

    condition = weather_description.get(
        weather_code,
        "Unknown weather condition"
    )

    return {
        "city": city.title(),
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

# if __name__ == "__main__":
#     result = get_weather("Goa")
#     print(result)