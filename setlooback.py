from typing import Any, Dict
import xml.dom.minidom
import sys
from ncclient import manager
import xmltodict

# NETCONF payload for configuring a Loopback interface
LOOPBACK_CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback100</name>
            <description>Configured via NETCONF</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>10.100.100.1</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""


def connect_to_device(
    host: str, username: str, password: str, port: int = 830
) -> manager.Manager:
  """Establishes a NETCONF connection to the device."""
  try:
    connection = manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,
        device_params={'name': 'csr'},
    )
    return connection
  except Exception as e:
    print(f"Failed to connect to {host}: {str(e)}")
    sys.exit(1)


def configure_loopback(connection: manager.Manager) -> Dict[str, Any]:
  """Pushes Loopback configuration using NETCONF."""
  try:
    response = connection.edit_config(target='running', config=LOOPBACK_CONFIG)
    # print(response.xml)
    return xmltodict.parse(response.xml)
  except Exception as e:
    print(f"Failed to configure loopback: {str(e)}")
    return {}


def display_result(result_data: Dict[str, Any]) -> None:
  """Displays the result of the NETCONF edit-config operation."""
  print(result_data)
  try:
    if 'ok' in result_data['rpc-reply']:
      print("\nLoopback100 configured successfully (<ok/> received).")
  except KeyError as e:
    print(f"Error parsing response data: {str(e)}")


def main():
  # Device connection parameters
  device = {
      'host': '172.16.132.129',  # CSR 1000v IP (change to 172.16.132.130 for router 2)
      'username': 'cisco',
      'password': 'cisco',
      'port': 830,
  }

  # Establish connection
  with connect_to_device(**device) as conn:
    print(f"Successfully connected to {device['host']}")

    # Configure loopback and display the result
    result_data = configure_loopback(conn)
    display_result(result_data)


if __name__ == '__main__':
  main()