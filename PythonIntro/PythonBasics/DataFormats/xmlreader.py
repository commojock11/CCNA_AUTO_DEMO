import xmltodict

with open('r1.xml') as file:
    xml_data = file.read()

data = xmltodict.parse(xml_data)

print(data['router']['routing']['routes']['route'][1]['destination'])
