import requests
import json

base_url = "https://swapi.dev/api/"
endpount = "people/"

response = requests.get(base_url + endpount)
# print(response)
# print("TEXT:")
# print(response.text)
# print("Status Code:")
# print(response.status_code)
# print("Headers:")
# print(response.headers)

data = response.json()
print(data["results"][4])
