import requests
import configparser
from pprint import pprint

config = configparser.ConfigParser()
config.read('config.ini')

sheety_prices_endpoint = str(config['sheety']['SHEETY_PRICES_ENDPOINT'])
sheety_token = str(config['sheety']['SHEETY_TOKEN'])
bearer_headers = {
    "Authorization": f"Bearer {sheety_token}"
}
# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_prices_endpoint, headers=bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            print(response.text)
