from utils.city_lookup import get_destination


def redirect_to_booking(from_city, to_city):

    #normalizing the inputs
    from_destination = get_destination(from_city)
    to_destination = get_destination(to_city)

    if not from_destination or not to_destination:
        return "❌ Sorry, I can't generate a booking link for this route."

    from_code = from_destination.get("iata")
    to_code = to_destination.get("iata")


    if not from_code or not to_code:
        return "❌ Sorry, I can't generate booking link for this route."

    from datetime import datetime
    # for current date when booking needs for accurate booking details 
    date = datetime.now().strftime("%Y-%m-%d")

    url = f"https://www.skyscanner.co.in/routes/{from_code.lower()}/{to_code.lower()}/"
    import webbrowser
    webbrowser.open(url)

    return f"🔗 Opening booking page for {from_city} → {to_city}...\n{url}"



if __name__ == "__main__":
    result = redirect_to_booking("Hyderabad", "Goa")
    print(result)