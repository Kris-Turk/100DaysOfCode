import requests
import datetime as dt

MY_LAT = -40.365400
MY_LNG = 175.664000

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.json()["iss_position"])

date = dt.datetime.now().date()

r = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
data = r.json()