from ncclient import manager
import xmltodict
import sys
from typing import Dict, Any, Optional

# NETCONF filter for interface information
INTERFACE_FILTER = '''
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name/>
            <description/>
            <enabled/>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip/>
                    <netmask/>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</filter>
'''

def connect_to_device(host: str, username: str, password: str, port: int = 830) -> Optional[manager.Manager]:
    """
    Establishes a NETCONF connection to the device.
    """
    try:
        connection = manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': 'csr'},
            timeout=30
        )
        return connection
    except Exception as e:
        print(f"Failed to connect to {host}: {str(e)}")
        return None

def get_interfaces(connection: manager.Manager) -> Dict[str, Any]:
    """
    Retrieves interface information using NETCONF.
    """
    try:
        response = connection.get(INTERFACE_FILTER)
        return xmltodict.parse(response.xml)
    except Exception as e:
        print(f"Failed to retrieve interface information: {str(e)}")
        return {}

def display_interfaces(host: str, interfaces_data: Dict[str, Any]) -> None:
    """
    Displays interface information in a format similar to 'show ip int brief'.
    """
    print(f"\n=== Router: {host} ===")
    print(f"{'Interface':<22}{'IP Address':<20}{'Status'}")
    print("-" * 60)
    
    try:
        interfaces = interfaces_data['rpc-reply']['data']['interfaces']['interface']
        if not isinstance(interfaces, list):
            interfaces = [interfaces]
            
        for interface in interfaces:
            name = interface.get('name', 'N/A')
            status = "up" if interface.get('enabled') == 'true' else "down"
            
            ip_address = "not assigned"
            ipv4_container = interface.get('ipv4')
            if isinstance(ipv4_container, dict) and 'address' in ipv4_container:
                addresses = ipv4_container['address']
                if isinstance(addresses, list):
                    ip_address = addresses[0].get('ip', 'not assigned')
                elif isinstance(addresses, dict):
                    ip_address = addresses.get('ip', 'not assigned')
            
            print(f"{name:<22}{ip_address:<20}{status}")
    
    except (KeyError, TypeError) as e:
        print(f"Error parsing interface data on {host}: {str(e)}")

def main():
    # Both CSR 1000v routers on the EVE-NG Management(Cloud0) subnet
    routers = [
        "172.16.132.129",
        "172.16.132.130"
    ]
    
    username = "cisco"
    password = "cisco"
    port = 830

    for host in routers:
        conn = connect_to_device(host=host, username=username, password=password, port=port)
        if conn:
            with conn:
                print(f"Successfully connected to {host}")
                interfaces_data = get_interfaces(conn)
                if interfaces_data:
                    display_interfaces(host, interfaces_data)

if __name__ == "__main__":
    main()