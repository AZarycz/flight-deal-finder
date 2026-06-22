import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
class FlightSearch:
    def __init__(self):
        self.serp_api_key=os.getenv('SERP_API_KEY')

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "api_key": self.serp_api_key,
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "currency": "EUR",
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d")
        }

        results = GoogleSearch(query)
        flights_data = results.get_dict()
        if "error" in flights_data:
            print(f"API error: {flights_data['error']}")
            return None
        return flights_data



