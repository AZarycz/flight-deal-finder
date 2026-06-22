import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv('ACCOUNT_SID')
        self.auth_token_twilio = os.getenv('AUTH_TOKEN_TWILIO')
        self.from_number = os.environ.get("TWILIO_FROM")
        self.to_number = os.environ.get("TWILIO_TO")

    def send_sms(self, price, iata_origin, iata_destination, from_date, to_date):
        client = Client(self.account_sid, self.auth_token_twilio)
        message = client.messages.create(
            body=f"Low price alert! Only {price} euro to fly from {iata_origin} to {iata_destination}, on {from_date} until {to_date}",
            from_=self.from_number,
            to=self.to_number,
        )
        print(message.status)
        return message