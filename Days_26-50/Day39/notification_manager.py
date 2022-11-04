from twilio.rest import Client
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TWILIO_SID = str(config['twilio']['account_sid'])
TWILIO_AUTH_TOKEN = str(config['twilio']['auth_token'])
TWILIO_VIRTUAL_NUMBER = str(config['twilio']['my_twilio_number'])
TWILIO_VERIFIED_NUMBER = str(config['twilio']['my_own_number'])

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)