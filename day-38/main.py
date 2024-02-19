import os
import requests
import datetime
import json


from dotenv import load_dotenv #Can be commented out in Live
load_dotenv() #Can be commented out in Live


GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 165
AGE = 35

sheety_endpoint = "https://api.sheety.co/3eb0925dddee722a203509e0ad58f6d7/workouts/workouts"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_ID")
S_TOKEN = os.getenv("SHEET_TOKEN")

exercise_text = input('What exercise did you do today?')

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

nutritionix_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


r = requests.post(nutritionix_endpoint, headers=nutritionix_headers,json=nutritionix_body)
result = r.json()
print(result)

for item in result['exercises']:
    now = datetime.datetime.now()
    # sheety_headers = {"Content-Type": "application/json"}
    sheety_headers = { "Authorization": f'Bearer {S_TOKEN}' }
    sheety_body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": item['name'].title(),
            "duration": item['duration_min'] ,
            "calories": item['nf_calories']
        }
    }
    json_data = json.dumps(sheety_body)
    sheety_r = requests.post(url=sheety_endpoint, headers=sheety_headers,json=sheety_body)
    sheety_r.json()
    
    print(sheety_r.text)
    

    