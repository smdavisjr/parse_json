import json
with open('test_dictionary.json') as file:
    data = json.load(file)

# import collections
# data2 = collections.OrderedDict(data)
# for ordered_data in data2:
    # print(ordered_data)
#
# for order in data:
#     print(order)

# (k, v, k2, v2), = data.items()
# k, v, k2, v2

import sys
json_str = json.dumps(data)
resp = json.loads(json_str)

# print (resp)
print (resp['currency']['USD'])
