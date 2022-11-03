import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

sheety_endpoint = str(config['sheety']['SHEETY_ENDPOINT'])
sheety_token = str(config['sheety']['SHEETY_TOKEN'])
bearer_headers = {
    "Authorization": f"Bearer {sheety_token}"
}
# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=sheety_endpoint, headers=bearer_headers )
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            print(response.text)
    
   
    