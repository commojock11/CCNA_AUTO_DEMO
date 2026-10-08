import requests
import json

# Suppress warnings for unverified HTTPS requests
requests.packages.urllib3.disable_warnings()

# Device details and credentials
DEVICE_IP = "devnetsandboxiosxec8k.cisco.com"
USERNAME = "clay.richards2222" # Update if using a different local lab account
PASSWORD = "B92_eXmw-97S5zK"

# RESTCONF endpoint for IETF standard interfaces
url = f"https://{DEVICE_IP}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

# Headers explicitly asking for JSON format
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

try:
    # Execute the GET request
    response = requests.get(
        url,
        auth=(USERNAME, PASSWORD),
        headers=headers,
        verify=False # Bypasses strict SSL certificate checking
    )
    
    # Check if the request was successful
    response.raise_for_status()

    # Parse and print the formatted JSON response
    response_data = response.json()
    print(json.dumps(response_data, indent=4))

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")