import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")

url = "https://serpapi.com/search.json"

params = {
    "engine": "google_hotels",
    "q": "Goa",
    "check_in_date": "2026-10-10",
    "check_out_date": "2026-10-13",
    "adults": 2,
    "currency": "INR",
    "gl": "in",
    "hl": "en",
    "api_key": API_KEY
}

response = requests.get(url, params=params)

print("Status:", response.status_code)

data = response.json()

properties = data.get("properties", [])

print("Number of hotels:", len(properties))

for hotel in properties:
    print("\n-------------------------")
    print("Name:", hotel.get("name"))
    print("Rating:", hotel.get("overall_rating"))
    print("Reviews:", hotel.get("reviews"))
    print("Price:", hotel.get("rate_per_night"))
    print("Total:", hotel.get("total_rate"))
    print("Location:", hotel.get("location"))
    print("Link:", hotel.get("link"))