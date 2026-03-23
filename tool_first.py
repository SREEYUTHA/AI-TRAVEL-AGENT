
def search_flights(source: str, destination: str):
    return f"Cheapest flight from {source} to {destination} costs Rs.4500"


def search_hotels(city:str):
    return f"Recommended hotel in {city}: Taj Residency, Rs.3000 per night."

def generate_itinerary(city:str, days:int):
    itinerary = {
        1: "Red Fort and Chandni Chowk",
        2: "Qutub Minar and India Gate",
        3: "Lotus Temple and Akshardham Temple"
    }

    plan = ""
    for day in range(1, days + 1):
        plan += f"Day {day}: {itinerary.get(day, 'Explore the city')}\n"
    
    return plan
