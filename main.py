#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests_cache
from data_manager import DataManager
from flight_data import find_cheapest_flight, FlightData
from flight_search import FlightSearch
from datetime import timedelta, date
from notification_manager import NotificationManager

# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 5 * 3600,
    }
)
# ==================== Set the Dates ====================
from_date = date(2026, 11, 15)
to_date = date(2026, 11, 21)
to_date_formatted = to_date.strftime("%Y-%m-%d")

# ==================== Talk to Sheety ====================
data_manager = DataManager()
sheety_data = data_manager.get_data()

# ==================== Do a Flight Search ====================
flights_found = FlightSearch()
notification = NotificationManager()

def flight_search(flight_searcher, origin_city, sheety_value):
    cheapest_overall = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    outbound_option = [from_date + timedelta(i) for i in range(3)]
    inbound_option = [to_date - timedelta(i) for i in range(3)]

    for outbound in outbound_option:
        for inbound in inbound_option:
            found_flights = flight_searcher.check_flights(
                destination_city_code=sheety_value["iataCode"],
                origin_city_code=origin_city,
                from_time=outbound,
                to_time=inbound
            )
            candidate = find_cheapest_flight(found_flights, inbound.strftime("%Y-%m-%d"))
            if candidate.price != "N/A":
                if cheapest_overall.price == "N/A" or candidate.price < cheapest_overall.price:
                    cheapest_overall = candidate

    return cheapest_overall

for value in sheety_data:
    print(value, "val")
    if value["iataCode"] == "BVA":
        origin = "POZ"
    else:
        origin = "BER"
    cheapest = flight_search(flights_found, origin, value)
    print(cheapest, "ch")

    # ==================== Show the Cheapest Flight ====================
    if cheapest.price == "N/A":
        print(f"Not found flight to {value['city']}")
    elif cheapest.price < value["lowestPrice"]:
        data_manager.update_lowest_price(
            value["city"],
            value["iataCode"],
            cheapest.price,
            value["id"]
        )
        print(f"Price to {value['city']} updated, new price: {cheapest.price}")
        notification.send_sms(cheapest.price, origin, value["iataCode"], cheapest.out_date, cheapest.return_date)
    else:
        print(f"No cheapest flight to {value['city']} found. Actual price: {cheapest.price}")




