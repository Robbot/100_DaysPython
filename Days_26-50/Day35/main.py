import requests
from twilio.rest import Client

MY_LAT = 56.673969
MY_LONG = 12.857290
api_key = "xxxxxxxxxxxxxxxxxx" #api key from openweather.com
account_sid = os.environ['TWILIO_ACCOUNT_SID'] #twilio account data
auth_token = os.environ['TWILIO_AUTH_TOKEN'] #twillio account token

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])

will_rain = False

weather_slice = weather_data["list"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+15017122661',
        to='+15558675310'
    )
    print(message.status)