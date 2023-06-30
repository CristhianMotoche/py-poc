import json
import xmltodict

def saveJson(entry, k):
    jsonString = json.dumps(entry)

    fileName = 'output' + str(k) + '.json'
    with open(fileName,'w') as fileJSON:
        fileJSON.write(jsonString)
    fileJSON.close()

with open('sample.xml', 'r') as fileXML:
    xmlString = fileXML.read()
fileXML.close()

print('XML input (sample.xml):')
print(xmlString)

xmlDictionary = xmltodict.parse(xmlString)
entries = xmlDictionary['uniprot']['entry']

k = 0
for entry in entries:
    k += 1
    saveJson(entry, k)

