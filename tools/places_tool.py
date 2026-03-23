import requests
import os
from tools.map_tool import get_coordinates
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEOAPIFY_API_KEY")

'''
def get_coordinates(city):
    url = "https://api.geoapify.com/v1/geocode/search"

    params = {
        "text": city,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "features" not in data or not data["features"]:
        return None

    coords = data["features"][0]["geometry"]["coordinates"]
    return coords  # [lon, lat]
'''

def get_places(city):
    """
    Fetch real tourist places using Geoapify API
    """

    coords = get_coordinates(city)

    if not coords:
        return f"❌ Could not find location for {city}"

    lon, lat = coords

    url = "https://api.geoapify.com/v2/places"

    params = {
        #"categories": "tourism.sights",
        "categories": "tourism.sights,tourism.attraction",
        "filter": f"circle:{lon},{lat},15000",  # 5km radius
        "limit": 5,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "features" not in data or not data["features"]:
        return f"❌ No places found in {city}"

    result = f"📍 Top places to visit in {city.title()}:\n\n"

    count = 0
    for i, place in enumerate(data["features"], 1):
        #name = place["properties"].get("name", "Unknown place")
        name = place["properties"].get("name")

        if not name:
            continue

        count += 1
        result += f"{count}. {name}\n"

        if count == 5:
            break
        result += f"{i}. {name}\n"

    

    return result