"""Basic Cisco DevNet DNA Center example: authenticate and list devices."""

import os
import sys

import requests
from requests.auth import HTTPBasicAuth


def main():
	host = os.getenv("DNAC_HOST", "https://sandboxdnac.cisco.com").rstrip("/")
	username = os.getenv("DNAC_USERNAME")
	password = os.getenv("DNAC_PASSWORD")

	if not username or not password:
		sys.exit("Set DNAC_USERNAME and DNAC_PASSWORD environment variables.")

	try:
		auth_response = requests.post(
			f"{host}/dna/system/api/v1/auth/token",
			auth=HTTPBasicAuth(username, password),
			timeout=15,
		)
		auth_response.raise_for_status()
		token = auth_response.json()["Token"]

		response = requests.get(
			f"{host}/dna/intent/api/v1/network-device",
			headers={"X-Auth-Token": token},
			timeout=15,
		)
		response.raise_for_status()
		devices = response.json().get("response", [])
	except requests.RequestException as error:
		sys.exit(f"DevNet API request failed: {error}")
	except (ValueError, KeyError):
		sys.exit("The DevNet API returned an unexpected response.")

	print(f"Found {len(devices)} device(s):")
	for device in devices:
		print(
			f"- {device.get('hostname', 'unknown')} "
			f"({device.get('managementIpAddress', 'no IP address')})"
		)


if __name__ == "__main__":
	main()
