from urllib import response

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")

# API_KEY = os.getenv("SERPAPI_KEY")

print("SERPAPI KEY LOADED:", bool(API_KEY))
print("SERPAPI KEY PREFIX:", API_KEY[:8] if API_KEY else None)

'''
def get_hotels(city, checkin, checkout, adults=1):
    """
    Search available hotels for a city and date range.
    """

    url = "https://api.stayingapi.com/v1/search"

    params = {
        "location": f"{city}, IN",
        "checkIn": checkin,
        "checkOut": checkout,
        "adults": adults,
        "platforms": "booking",
        "limit": 5
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers
    )

    data = response.json()

    if response.status_code != 200:
        return {
            "city": city,
            "checkin": checkin,
            "checkout": checkout,
            "environment": "sandbox",
            "hotels": [],
            "error": data.get("error", data)
        }

    hotels = []

    for hotel in data.get("data", []):

        price = hotel.get("price", {})

        hotels.append({
            "name": hotel.get("name"),
            "rating": hotel.get("guestRating"),
            "rating_scale": hotel.get("ratingScale"),
            "price_per_night": price.get("nightlyPrice"),
            "total_price": price.get("totalPrice"),
            "currency": price.get("currency"),
            "booking_url": hotel.get("url")
        })

    return {
        "city": city,
        "checkin": checkin,
        "checkout": checkout,
        "adults": adults,
        "environment": "sandbox",
        "warning": "These are sandbox test results and are not real destination-specific hotel recommendations.",
        "hotels": hotels
    }
'''
def get_hotels(city, checkin, checkout, adults=1):

    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_hotels",
        "q": city,
        "check_in_date": checkin,
        "check_out_date": checkout,
        "adults": adults,
        "currency": "INR",
        "gl": "in",
        "hl": "en",
        "api_key": API_KEY
    }

    # debugging print statements
    print("\n===== HOTEL TOOL =====")
    print("City:", city)
    print("Check-in:", checkin)
    print("Check-out:", checkout)
    print("Adults:", adults)
    print("API key loaded:", bool(API_KEY))

    response = requests.get(url, params=params)

    print("SerpApi status:", response.status_code)
    print("SerpApi response:", response.text[:1000])

    print("Status:", response.status_code)

    data = response.json()

    properties = data.get("properties", [])

    hotels = []

    for hotel in properties:

        price = hotel.get("rate_per_night", {})
        total = hotel.get("total_rate", {})

        hotels.append({
            "name": hotel.get("name"),
            "rating": hotel.get("overall_rating"),
            "reviews": hotel.get("reviews"),
            "price_per_night": price.get("extracted_lowest"),
            "total_price": total.get("extracted_lowest"),
            "currency": "INR",
            "booking_url": hotel.get("link")
        })

    return {
        "city": city,
        "checkin": checkin,
        "checkout": checkout,
        "adults": adults,
        "hotels": hotels
    }

if __name__ == "__main__":

    result = get_hotels(
        "Goa",
        "2026-10-10",
        "2026-10-13",
        2
    )

    print(result)