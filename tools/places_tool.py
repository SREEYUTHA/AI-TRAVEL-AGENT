import requests
import os
from tools.map_tool import get_coordinates
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEOAPIFY_API_KEY")


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
        "categories": (
            "tourism.sights.archaeological_site,"
            "tourism.sights.castle,"
            "tourism.sights.fort,"
            "tourism.sights.monastery,"
            "tourism.sights.tower,"
            "tourism.sights.ruines,"
            "tourism.sights.place_of_worship,"
            "tourism.attraction"
        ),
        "filter": f"circle:{lon},{lat},30000",
        "bias": f"proximity:{lon},{lat}",
        "limit": 20,
        "apiKey": API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "features" not in data or not data["features"]:
        return f"❌ No places found in {city}"

    result = f"📍 Tourist places found in {city.title()}:\n\n"

    seen = set()
    places = []

    for place in data["features"]:
        properties = place["properties"]

        name = properties.get("name")
        categories = properties.get("categories", [])

        # Ignore unnamed places
        if not name:
            continue

        # Ignore duplicates
        if name in seen:
            continue

        seen.add(name)

        # Give higher priority to important sightseeing categories
        score = 0

        if "tourism.sights.archaeological_site" in categories:
            score += 6

        if "tourism.sights.castle" in categories:
            score += 6

        if "tourism.sights.fort" in categories:
            score += 6

        if "tourism.sights.ruines" in categories:
            score += 5

        if "tourism.sights.place_of_worship" in categories:
            score += 4

        if "tourism.attraction" in categories:
            score += 3

        if "tourism.sights" in categories:
            score += 2

        # Reduce priority for memorials/statues/artwork
        if "tourism.sights.memorial" in categories:
            score -= 4

        if "tourism.attraction.artwork" in categories:
            score -= 3

        if "tourism.attraction.artwork.statue" in categories:
            score -= 5
    
        places.append((score, name))

    # Sort by score
    places.sort(reverse=True)

    # Take top 5
    for count, (_, name) in enumerate(places[:8], 1):
        result += f"{count}. {name}\n"

    return result


if __name__ == "__main__":
    result = get_places("Delhi")
    print(result)