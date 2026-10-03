import requests
import os
from dotenv import load_dotenv
load_dotenv()

# API_KEY = "3bdaacd9b9cb4f1fae910e3276806b5a"
API_KEY = os.getenv("GEOAPIFY_API_KEY")

def get_coordinates(city):
    url = "https://api.geoapify.com/v1/geocode/search"

    params = {
        "text": f"{city}, India",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # ✅ FIRST TRY
    if "features" in data and data["features"]:
        return data["features"][0]["geometry"]["coordinates"]

    # 🔁 SECOND TRY (add India)
    # params["text"] = f"{city}, India"
    # response = requests.get(url, params=params)
    # data = response.json()

    if "features" in data and data["features"]:
        return data["features"][0]["geometry"]["coordinates"]

    return None


def get_route_info(from_city, to_city):
    start = get_coordinates(from_city)
    end = get_coordinates(to_city)

    if not start or not end:
        return "Location not found"

    url = "https://api.geoapify.com/v1/routing"

    params = {
        "waypoints": f"{start[1]},{start[0]}|{end[1]},{end[0]}",
        "mode": "drive",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "features" not in data:
        return f"Error: {data}"

    distance = data["features"][0]["properties"]["distance"] / 1000
    time = data["features"][0]["properties"]["time"] / 3600

    return f"Distance: {distance:.2f} km, Duration: {time:.2f} hours"

'''
if __name__ == "__main__":
    result = get_route_info("Hyderabad", "Goa")
    print(result)
'''