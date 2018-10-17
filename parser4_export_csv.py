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
columnTitleRow = "region, is_active, status\n"
csv.write(columnTitleRow)

for key in resp:
    region = key
    status = str(resp[region]['general']['active'])
    active_test = 'active' if status == 'True' else 'non-active'
    row = region + "," + status + "," + active_test + "\n"
    csv.write(row)

print ('Export successful')
