import requests

OWM_API = "https://api.openweathermap.org/data/2.5/weather"
APPID = '5c92ba756bb54b2f0506d931d6b057f4'

parameters = {
    "q": "Wellington",
    "appid": APPID
}

r = requests.get(OWM_API, params=parameters)
print(r.status_code)