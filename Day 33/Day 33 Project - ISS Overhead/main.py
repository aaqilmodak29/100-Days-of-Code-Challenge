import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 19.075983  # Your latitude
MY_LONG = 72.877655  # Your longitude
MY_EMAIL = ""  # Your email
PASSWORD = ""  # Your password

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def position_of_iss():
    if 67 <= iss_longitude <= 77 and 14 <= iss_latitude <= 24:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    # Run the code every 60 seconds.
    time.sleep(60)
    if position_of_iss() and time_now.hour <= sunrise or time_now.hour >= sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up!\n\n"
                                                                                      "The ISS is Overhead")
