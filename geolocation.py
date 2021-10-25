import sys
import csv
import requests

#target is a CSV file that includes some pairs of BSSIDs.
target = sys.argv[1]

API_key = "API_key"

with open(target,encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        bssid_1 = row[0]
        bssid_2 = row[1]
        payload =         {
           "wifiAccessPoints": [{
                "macAddress": bssid_1
            }, {
                "macAddress": bssid_2
            }]
        }
        r = requests.post('https://location.services.mozilla.com/v1/geolocate?key='+ API_key, json=payload)
        latlng = r.json()['location']
        lat = latlng['lat']
        lng = latlng['lng']
        print('lat : ' +str(lat))
        print('lat : ' +str(lng))
        print('==================')
        with open('result_'+target,'a') as f:
            writer = csv.writer(f,lineterminator = '\n')
            csvlist = []
            csvlist.append(lat)
            csvlist.append(lng)
            writer.writerow(csvlist)