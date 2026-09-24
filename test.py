import webbrowser

'''
webbrowser.open("https://www.google.com")
'''

def redirect_to_booking(from_city, to_city):
    iata_map = {
        "Hyderabad": "HYD",
        "Delhi": "DEL",
        "Mumbai": "BOM",
        "Bangalore": "BLR",
        "Chennai": "MAA"
    }

    # normalize input
    from_city = from_city.title()
    to_city = to_city.title()

    from_code = iata_map.get(from_city)
    to_code = iata_map.get(to_city)

    if not from_code or not to_code:
        return "❌ Invalid city name"

    url = f"https://www.skyscanner.co.in/transport/flights/{from_code}/{to_code}/260420/"

    webbrowser.open(url)

    return f"Opening booking page for {from_city} → {to_city}"

source = input("Enter source city: ")
destination = input("Enter destination city: ")

print(redirect_to_booking(source, destination))