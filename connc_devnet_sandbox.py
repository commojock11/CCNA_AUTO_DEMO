from typing import Any, Dict
import xml.dom.minidom
import sys
from ncclient import manager
import xmltodict

# NETCONF filter for live operational interface information (includes DHCP IPs)
INTERFACE_FILTER = """
<interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
        <name/>
        <ipv4/>
        <admin-status/>
        <oper-status/>
    </interface>
</interfaces>
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


def get_interfaces(connection: manager.Manager) -> Dict[str, Any]:
  """Retrieves interface information using NETCONF."""
  try:
    response = connection.get(filter=('subtree', INTERFACE_FILTER))
    # print(response.xml)
    return xmltodict.parse(response.xml)
  except Exception as e:
    print(f"Failed to retrieve interface information: {str(e)}")
    return {}


def display_interfaces(interfaces_data: Dict[str, Any]) -> None:
  """Displays interface information in a format similar to 'show ip int brief'."""
  print(interfaces_data)
  print("\nInterface\t\tIP Address\t\tStatus")
  print("-" * 60)

  try:
    interfaces = interfaces_data['rpc-reply']['data']['interfaces']['interface']
    if not isinstance(interfaces, list):
      interfaces = [interfaces]

    for interface in interfaces:
      name = interface.get('name', 'N/A')
      status = 'up' if 'up' in interface.get('admin-status', '') else 'down'

      ip_address = interface.get('ipv4', 'not assigned')
      if ip_address == '0.0.0.0' or not ip_address:
        ip_address = 'not assigned'

      print(f'{name:<24}{ip_address:<20}{status}')

  except KeyError as e:
    print(f'Error parsing interface data: {str(e)}')


def main():
  # Cisco DevNet Catalyst 8000V Sandbox connection parameters
  device = {
      'host': 'devnetsandboxiosxec8k.cisco.com',
      'username': 'clay.richards2222',
      'password': 'd3FcKk0_PP4Rs_s5',
      'port': 830,
  }

  # Establish connection
  with connect_to_device(**device) as conn:
    print(f"Successfully connected to {device['host']}")

    # Get and display interface information
    interfaces_data = get_interfaces(conn)
    display_interfaces(interfaces_data)


if __name__ == '__main__':
  main()