import json
from pprint import pprint

with open('production.json') as file:
    data = json.load(file)

# pprint(data['ABE']['general']['active'])
# pprint(data['ABE']['general']['applicantDriverDocs'][0])

data.keys()
for key in data.keys():
    # is_active = (key[5][0])
    is_active = key

    # is_active = (['key']['general']['active'])
    print(is_active)
# print(is_active)
