import requests
import os
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

parameters = {
    "lat": -40.365398,
    "lon": 175.664001,
    "appid": os.getenv('appid'),
    "exclude": "current,minutely,daily"
}


account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid,auth_token)



r = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

hourly = r.json()['hourly']

def is_going_to_rain(hourly_weather_data,next_hours):
    for hour in hourly_weather_data[0:next_hours-1]:
        if hour["weather"][0]["main"] == "Rain":
            return True
        
        
if is_going_to_rain(hourly,24):
    # print("Shit its going to rain today!")
    message = client.messages \
                .create(
                     body="Shit its going to rain today!",
                     from_='+17792092661',
                     to='+64272042978'
                 )
    # print(message.sid)
    
else:
    print("We cool, no rain today")
    message = client.messages \
            .create(
                    body="We cool, no rain today",
                    from_='+17792092661',
                    to='+64272042978'
                )