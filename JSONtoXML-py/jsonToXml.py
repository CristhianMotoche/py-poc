import json
import xmltodict

with open('sample.json', 'r') as f:
    jsonString = f.read()

print('JSON input (sample.json):')
print(jsonString)

xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)

print('\nXML output(output.xml):')
print(xmlString)

with open('output.xml', 'w') as f:
    f.write(xmlString)
