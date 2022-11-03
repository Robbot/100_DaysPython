import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = str(config['kiwi']['api_key'])


class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code
