import json
with open('test_dictionary.json') as file:
    data = json.load(file)

for key, value in data.items():
    # if "Canada" == value:
    print key[1]
