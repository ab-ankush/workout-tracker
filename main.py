import requests
from datetime import datetime
from env import *


exercise = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


parameters1 = {
    "query": exercise,
}

exc_response = requests.post(url=exercise_endpoint,
                             json=parameters1, headers=headers)
result = exc_response.json()


# print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

today = datetime.now()
date = today.strftime("%m/%d/%Y")
time = today.strftime("%H:%M:%S")

headers2 = {
    "Authorization": secret
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(
        url=sheety_endpoint, json=sheet_inputs, headers=headers2)

    print(sheety_response.text)
