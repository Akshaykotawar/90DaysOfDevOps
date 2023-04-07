"""For read Json File"""
import json
f = open('services.json')
data = json.load(f)
#print(data['services']['aws']['name'])
for key, value in data['services'].items():
    if key != 'debug':
        print(key,":",data['services'][key]['name'])
#output of above loop
for key, value in data['services'].items():
    if key != 'debug':
        print(key,":",data['services'][key]['name'])

"""For Read Yaml File"""
import yaml
f = open(r"C:\Users\akshay kotawar\PycharmProject\90daysdevopschallenge\2023\day15\services.yaml")
data = yaml.safe_load(f)
for key, value in data['services'].items():
    if key != 'debug':
        print(key,":",data['services'][key]['name'],', instannces :',data['services'][key]['instances'])

#output of above loop is
aws : EC2 , instannces : 500
azure : VM , instannces : 500
gcp : Compute Engine , instannces : 500