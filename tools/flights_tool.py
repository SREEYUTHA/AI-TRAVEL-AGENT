import requests
import os
from dotenv import load_dotenv
from utils.city_lookup import get_destination

load_dotenv()

# from tools.places_tool import API_KEY


API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
print("API key loaded:", API_KEY is not None)

def get_flights(from_city, to_city):
    """
    Fetch basic flight data between cities
    """

    from_destination = get_destination(from_city)
    to_destination = get_destination(to_city)

    if not from_destination or not to_destination:
        return "❌ Sorry, I don't recognize one of the cities."


    from_code = from_destination.get("iata")
    to_code = to_destination.get("iata")

    if not from_code or not to_code:
        return "❌ Sorry, I don't recognize one of the cities."

    url = "https://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "dep_iata": from_code,
        "arr_iata": to_code,
        "limit": 5,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "data" not in data:
        return f"Error: {data}"

    flights = data["data"]

    if not flights:
        return "No flights found"

    result = []

    for flight in flights:
        dep = flight.get("departure", {}).get("iata")
        arr = flight.get("arrival", {}).get("iata")

        if dep != from_code or arr != to_code:
            continue

        airline = flight.get("airline", {}).get("name")
        flight_no = flight.get("flight", {}).get("iata")
        status = flight.get("flight_status")

        result.append({
            "airline": airline,
            "flight_number": flight_no,
            "status": status,
        })

    return result


'''
if __name__ == "__main__":
    result = get_flights("Hyderabad", "Mumbai")
    print(result)
'''