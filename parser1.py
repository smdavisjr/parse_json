import json
from pprint import pprint

with open('production.json') as file:
    data = json.load(file)

pprint(data['ABE']['general']['active'])
# pprint(data['ABE']['general']['applicantDriverDocs'][0])
#
# data.keys()
# for key in data.keys():
#     is_active = (key[5][0])
#     break
# pprint(is_active)
#     # if ((key[5][1]) == 'true'): print(key)
#
#     # break
#     # print key if (key[5][1]) == 'true'
# # print(key)
#     # print(key)
# # print(is_active)
