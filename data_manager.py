import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_token = os.environ.get('SHEETY_TOKEN')
        self.sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')
        self.bearer_headers = {
            "Authorization": f"Bearer {self.sheety_token}"
        }
        self.lowest_price_data = []

    def get_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.bearer_headers)
        data = response.json()
        self.lowest_price_data = data["prices"]
        print(self.lowest_price_data, 'lowest')
        return self.lowest_price_data

    def update_lowest_price(self, city, code, new_price, row_id):
        prices = {
            'price' : {
                'city': city,
                'iataCode': code,
                'lowestPrice': new_price
            }
        }
        url_put = os.getenv('SHEETY_ENDPOINT')
        resp = requests.put(url=f'{url_put}/{row_id}', json=prices, headers=self.bearer_headers)
        return resp


