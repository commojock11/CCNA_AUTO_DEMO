import requests
import json
import urllib3

# Suppress warnings for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEVICE_IP = "172.16.132.130"
USERNAME = "cisco"
PASSWORD = "cisco"

# Target the specific interface we want to create or modify
url = f"https://{DEVICE_IP}/restconf/data/ietf-interfaces:interfaces/interface=Loopback2222"

# Headers must now specify both what we Accept back, and the Content-Type we are sending
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# The JSON payload matching the ietf-interfaces YANG model structure
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback2222",
        "description": "Automated Loopback via RESTCONF PUT",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.22.22.22",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

try:
    # Execute a PUT request instead of GET, passing in the json payload
    response = requests.put(
        url,
        auth=(USERNAME, PASSWORD),
        headers=headers,
        data=json.dumps(payload),
        verify=False 
    )
    
    # Check if the request was successful (HTTP 2xx)
    response.raise_for_status()

    # PUT requests typically return a 201 (Created) or 204 (No Content) on success with no body
    if response.status_code in [201, 204]:
        print(f"Success! Interface Loopback2222 is configured. (Status Code: {response.status_code})")
    else:
        print(f"Executed with status code: {response.status_code}")

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"A connection error occurred: {e}")