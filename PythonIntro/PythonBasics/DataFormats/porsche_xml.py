import xmltodict

with open("porsche.xml") as file:
    data = xmltodict.parse(file.read())
print(data)