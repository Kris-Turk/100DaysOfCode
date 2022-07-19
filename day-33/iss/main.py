import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()       

from_email = os.environ["FROM_EMAIL"]
password = os.environ["PASSWORD"]
MY_LAT = -40.365400
MY_LNG = 175.664000

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sun_data = response.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if iss_latitude >= MY_LAT -5 and iss_latitude <= MY_LAT +5 and iss_longitude >= MY_LNG -5 and iss_longitude <= MY_LNG +5:
    if time_now.hour > sunset and time_now.hour < sunrise:
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=from_email,password=password)
            conn.sendmail(f"Subject:Lookup\n\nThe ISS is above")
            

