import requests
# import os
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api = "Your API"
DATA= {
    'lat' : 28.613939,
    'lon': 77.209023,
    'appid' : api,
    'cnt' : 4,
}
account_sid ="Your Account ID"
auth_token ="Your Authentication Token"

response=  requests.get(ENDPOINT, params=DATA)
weather  = response.json()
# print(weather["list"][0]["weather"][0]["id"])
rain = False
for hour in weather["list"]:
    code = int(hour["weather"][0]["id"])
    if code < 700:
        rain = True

if rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's Going to Rain Today. Carry Umbrellaaa!!!!!!!!!!!!!!!!",
    from_="Provided number",
    to="Your number",
    )

    print(message.status)