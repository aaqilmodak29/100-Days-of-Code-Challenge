import requests
import os
import datetime as dt

now = dt.datetime.now()

today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = "male"
WEIGHT =  # your weight
HEIGHT =  # your height
AGE =  # your age
USER = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = os.environ.get("SHEET_ENDPOINT")

query = input("What exercise did you do today? ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
result = exercise_response.json()

for i in range(len(result["exercises"])):
    name_of_exercise = result["exercises"][i]["name"].title()
    duration = round(result["exercises"][i]["duration_min"])
    calories = round(result["exercises"][i]["nf_calories"])

    sheet_parameters = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": name_of_exercise,
            "duration": duration,
            "calories": calories
        }
    }

    sheet_response = requests.post(url=sheets_endpoint, json=sheet_parameters, auth=(USER, PASSWORD))
    sheet_result = sheet_response.json()
    print(sheet_result)

