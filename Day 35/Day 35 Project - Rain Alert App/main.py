import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = "" # your api key
MY_LAT = 19.075983
MY_LON = 72.877655
account_sid = "" # your account id
auth_token = "" # your auth token

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
for i in range(0, 12):
    if data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Its going to rain today, bring an umbrella",
        from_='', # twilio number,
        to='' # your number
    )
    print(message.status)
