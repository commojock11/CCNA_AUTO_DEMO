import json

# with open('r1.json') as file:
#     json_data = json.load(file)

router_json = '''
{
    "router": {
        "hostname": "R1",
        "interfaces": [
            {
                "id": "0",
                "enabled": "true",
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.254",
                "mask": "255.255.255.0"
            },
            {
                "id": "1",
                "enabled": "true",
                "name": "GigabitEthernet0/1",
                "ip": "172.16.1.2",
                "mask": "255.255.255.0"
            }
        ],
        "routing": {
            "routes": [
                {
                    "destination": "192.168.2.0",
                    "mask": "255.255.255.0",
                    "gateway": "192.168.1.253"
                },
                {
                    "destination": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "gateway": "201.1.113.54"
                }
            ]
        }
    }
}
'''
json_data = json.loads(router_json)


print(json_data['router']['interfaces'][1]['enabled'])
print(json_data['router']['routing']['routes'][1]['destination'])

# json.load() JSON -> Python File Load from a file
# json.loads() JSON -> Python String Load from a string
# json.dump() Python -> JSON File Dump into a file
# json.dumps() Python -> JSON String Dump as a string