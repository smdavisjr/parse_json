import json
import csv
# import sys
# from pprint import pprint

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

# #
# #
# # GET ALL REGION CODES AND ACTIVE STATUS
# print('region code, is active')
# print('-----')
# for key in resp:
#     region = key
#     status = (resp[region]['general']['active'])
#     print (region, status)
# print('-----')
# # print('')
# #
# #
# # CLASSIFICATION OF REGIONS AS ACTIVE OR NON-ACTIVE
# for key in resp:
#     region = key
#     active_test = 'active' if ((resp[region]['general']['active']) == 'true') else 'non-active'
#     # pprint (active_test)
#
# # while True:
# #     active_test = 'active'
# #     if (resp[region]['general']['active']) == 'true':
#         # break
#
# active_true = active_test.count('active')
# active_false = active_test.count('non-active')
# #
# #
# # COUNT OF ALL REGIONS
# print('count total:')
# print(len(data.keys()))
# # print('')
# print('-----')
# #
# #
# # COUNT OF ACTIVE REGIONS
# print('count active:')
# print(active_true)
# # print('')
# print('-----')
# #
# #
# # COUNT OF NON-ACTIVE REGIONS
# print('count not active:')
# print(active_false)
# # print('')
# print('-----')
# print('-----')


# active_true = active_test.count('true')
# active_false = active_test.count('false')
