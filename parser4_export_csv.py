import json
import csv
# import sys
## from pprint import pprint

with open('production.json') as file:
    data = json.load(file)
json_str = json.dumps(data)
resp = json.loads(json_str)

download_dir = 'testparser4.csv'
csv = open(download_dir, "w")
columnTitleRow = "region, status\n"
csv.write(columnTitleRow)

for key in resp:
    region = key
    status = str(resp[region]['general']['active'])
    row = region + "," + status + "\n"
    csv.write(row)

print ('Export successful')
