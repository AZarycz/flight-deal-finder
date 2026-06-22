class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, orig, dest, out, ret):
        self.price = price
        self.origin_airport = orig
        self.destination_airport = dest
        self.out_date = out
        self.return_date = ret

def find_cheapest_flight(flight_data, return_date_flight):
    if flight_data is None:
        return FlightData(
                price = "N/A",
                orig = "N/A",
                dest = "N/A",
                out = "N/A",
                ret = "N/A"
            )

    flights_best = flight_data.get('best_flights', [])
    flights_other = flight_data.get('other_flights', [])
    flights = flights_best+flights_other
    if not flights:
        return FlightData(
            price="N/A", orig="N/A", dest="N/A", out="N/A", ret="N/A"
        )
    cheapest_flight = FlightData(price=float("inf"), orig="", dest="", out="", ret="")

    for flight in flights:
        try:
            date_extracted = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            if flight["price"] < cheapest_flight.price:
                cheapest_flight = FlightData(
                    flight["price"],
                    flight["flights"][0]["departure_airport"]["id"],
                    flight["flights"][-1]["arrival_airport"]["id"],
                    date_extracted,
                    return_date_flight
                )


        except (KeyError, IndexError):
            continue
    return cheapest_flight

