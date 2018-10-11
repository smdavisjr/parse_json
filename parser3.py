import json
from pprint import pprint

with open('production.json') as file:
    data = json.load(file)

keys = data.keys()
values = data.values()

# print(list(keys))
# for key in keys:
# keys.get((key[0][0])['none'])

for key, value in data.items():
    if ([0]) == "ABE":
#     if ([key]['general']['active']) == 'true':
        print key
    else:
        print 'nope'
