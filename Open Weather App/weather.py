import requests
from datetime import datetime

url_curr = "https://community-open-weather-map.p.rapidapi.com/weather"
url_forecast = "https://community-open-weather-map.p.rapidapi.com/forecast"

city = input("Enter the city name and country code : ")

query = {"q": city, "units": "metric"}
query_forecast = {"q": city, "units": "metric", "cnt": 1}

headers = {
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": "e228ed9bcdmsha1fc0c3f1222c75p1d3eafjsn15f97a40c083"
}

response_curr = requests.request(
    'GET', url_curr, params=query, headers=headers)
res_forescast = requests.request(
    'GET', url_forecast, params=query_forecast, headers=headers)

print(f"\nCity name : {response_curr.json()['name']}")
print(f"City coordinates : {response_curr.json()['coord']}\n")

current_time = datetime.now()

current_hour = current_time.strftime("%I")
current_minute = current_time.strftime("%M")
current_seconds = current_time.strftime("%S")
current_period = current_time.strftime("%p")

print("Current Weather (Time : "+ datetime.now().strftime("%H:%M:%S %p")+") : ")
print(f"Weather Conditions : {response_curr.json()['weather'][0]['main']}, {response_curr.json()['weather'][0]['description']}")
print(f"Temperature : {response_curr.json()['main']['temp']}, min - {response_curr.json()['main']['temp_min']}, max - {response_curr.json()['main']['temp_max']}")
print(f"Pressure : {response_curr.json()['main']['pressure']} hPa")
print(f"Humidity : {response_curr.json()['main']['humidity']} %")
print(f"Visibility : {response_curr.json()['visibility']} m")
print(f"Wind : {response_curr.json()['wind']['speed']} km/hr, {response_curr.json()['wind']['deg']} degrees\n")


# print(res_forescast.text)
# i = 0
# if int(current_hour) + 3 > 12 and current_period != "PM":
#     current_period = "PM"
# elif int(current_hour) + 3 < 12 and current_period != "AM":
#     current_period = "AM"

# if int(current_hour) + 3 >= 24 :
#     current_hour = int(current_hour) + 3 - 24

print(f"3-Hour Weather Forecast : ")
print(f"Weather Conditions : {res_forescast.json()['list'][0]['weather'][0]['main']}, {res_forescast.json()['list'][0]['weather'][0]['description']}")
print(f"Temperature : {res_forescast.json()['list'][0]['main']['temp']}, min - {res_forescast.json()['list'][0]['main']['temp_min']}, max - {res_forescast.json()['list'][0]['main']['temp_max']}")
print(f"Pressure : {res_forescast.json()['list'][0]['main']['pressure']} hPa")
print(f"Humidity : {res_forescast.json()['list'][0]['main']['humidity']} %")
print(f"Visibility : {res_forescast.json()['list'][0]['visibility']} m")
print(f"Wind : {res_forescast.json()['list'][0]['wind']['speed']} km/hr, {res_forescast.json()['list'][0]['wind']['deg']} degrees\n")
