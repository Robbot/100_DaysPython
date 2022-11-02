import requests
import configparser
from twilio.rest import Client

config = configparser.ConfigParser()
config.read('config.ini')

MY_LAT = str(config['constants']['my_lat'])
MY_LONG = str(config['constants']['my_long'])
api_key = str(config['openweather']['api_key'])
account_sid = str(config['twilio']['account_sid'])
auth_token = str(config['twilio']['auth_token'])
send_from = str(config['twilio']['my_twilio_number'])
send_to = str(config['twilio']['my_own_number'])

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0])

will_rain = False

weather_slice = weather_data["list"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    #print("it will be raining")
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=send_from,
        to=send_to
    )
    print(message.status)