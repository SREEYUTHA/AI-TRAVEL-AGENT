def redirect_to_booking(from_city, to_city):

    #normalizing the inputs
    from_city = from_city.title().strip()
    to_city = to_city.title().strip()

    # as International Airport Transport Association (IATA) has three codes for getting city information 

    iata_map = {

    "Hyderabad": "HYD",
    "Delhi": "DEL",
    "Mumbai": "BOM",
    "Bangalore": "BLR",
    "Chennai": "MAA"
    }

    from_code = iata_map.get(from_city)
    to_code = iata_map.get(to_city)


    if not from_code:
        return "❌ Sorry, I can't generate booking link for this route."


    from datetime import datetime
    # for current date when booking needs for accurate booking details 
    date = datetime.now().strftime("%d%m%y")

    url = f"https://www.skyscanner.co.in/transport/flights/{from_code}/{to_code}/{date}/"

    import webbrowser
    webbrowser.open(url)

    return f"🔗 Opening booking page for {from_city} → {to_city}...\n{url}"