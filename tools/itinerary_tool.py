def create_itinerary(destination, duration, places):
    """
    Create a simple day-by-day travel itinerary.
    """

    itinerary = {}
    duration = int(str(duration).split()[0])
    
    for day in range(1, duration + 1):
        itinerary[f"Day {day}"] = []

    for index, place in enumerate(places):
        day = (index % duration) + 1
        itinerary[f"Day {day}"].append(place)
    
    return itinerary


'''
if __name__ == "__main__":
    places = [
        "Baga Beach",
        "Fort Aguada",
        "Dudhsagar Falls",
        "Basilica of Bom Jesus",
        "Calangute Beach"
    ]

    result = create_itinerary("Goa", 3, places)

    print(result)
'''