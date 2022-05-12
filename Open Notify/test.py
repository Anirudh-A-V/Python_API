import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')
res = requests.get('http://api.open-notify.org/iss-now.json')

# print(res.status_code)
print(f"\nPosition of the ISS : ({res.json()['iss_position']['longitude']}, {res.json()['iss_position']['latitude']})")
print(f"\nNo. of people in the ISS : {response.json()['number']}")

print("\nList of people in the ISS : ")
for i in response.json()['people']:
    print(i['name'])
