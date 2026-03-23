#Api_key = dfb5a20da10ba39da653003fbaf8796c

import requests
import os

API_KEY = "dfb5a20da10ba39da653003fbaf8796c"
#API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def get_flights(from_city, to_city):
    """
    Fetch basic flight data between cities
    """

    from_code = get_iata_code(from_city)
    to_code = get_iata_code(to_city)

    if not from_code or not to_code:
        return "❌ Sorry, I don't recognize one of the cities."

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "dep_iata": get_iata_code(from_city),
        "arr_iata": get_iata_code(to_city),
        "limit": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "data" not in data:
        return f"Error: {data}"

    flights = data["data"]

    if not flights:
        return "No flights found"

    '''    
    result = []

    for flight in flights[:5]:
        airline = flight["airline"]["name"]
        flight_no = flight["flight"]["iata"]
        status = flight["flight_status"]

        result.append(f"{airline} ({flight_no}) - {status}")

    #return "\n".join(result)
    '''
    result = []

    for flight in flights:
        dep = flight["departure"]["iata"]
        arr = flight["arrival"]["iata"]

        if dep != get_iata_code(from_city) or arr != get_iata_code(to_city):
            continue

        airline = flight["airline"]["name"]
        flight_no = flight["flight"]["iata"]
        status = flight["flight_status"]

        # add smart enhancements
        import random
        price = random.randint(3000, 8000)
        duration = random.choice(["2h 10m", "2h 30m", "1h 55m"])

        result.append(
            f"✈️ {airline} ({flight_no})\n"
            f"💰 ₹{price} | ⏱ {duration} | Status: {status}\n"
        )

        result_text = f"✈️ Flights from {from_city} to {to_city}:\n\n"

        for i, flight in enumerate(result[:5], 1):
            result_text += f"{i}.\n{flight}\n"

        return result_text


# simple mapping (for now)
def get_iata_code(city):
    city = city.strip().lower()

    mapping = {
        "hyderabad": "HYD",
        "delhi": "DEL",
        "mumbai": "BOM",
        "bangalore": "BLR",
        "bengaluru": "BLR",
        "chennai": "MAA"
    }

    code = mapping.get(city)

    if not code:
        return None

    return code