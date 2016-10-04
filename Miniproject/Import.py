import requests
import xmltodict

auth_details = ('gijsvg94@hotmail.com','2c8lAWJFo0Ac7dLdD-Uyk1fipmwTYb-5Lc-0jMu-MZBWhyrNIYDIdw')
api_url ='http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url,auth =auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]# 18:36
    print('Om '+vertrektijd+' vertrekt een trein naar '+eindbestemming)
