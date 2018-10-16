import json
import sys

with open('production.json') as file:
    data = json.load(file)

json_str = json.dumps(data)
resp = json.loads(json_str)

# GET ALL REGION CODES AND ACTIVE STATUS
print('region code, is active')
print('-----')
for key in resp:
    region = key
    status = (resp[region]['general']['active'])
    print (region, status)
print('-----')


# CLASSIFICATION OF REGIONS AS ACTIVE OR NON-ACTIVE
for key in resp:
    region = key
    active_test = 'active' if ((resp[region]['general']['active']) == 'true') else 'non-active'
    active_true = active_test.count('active')
    active_false = active_test.count('non-active')


# COUNT OF ALL REGIONS
print('count total:')
print(len(data.keys()))
print('-----')


# COUNT OF ACTIVE REGIONS
print('count active:')
print(active_true)
print('-----')


# COUNT OF NON-ACTIVE REGIONS
print('count not active:')
print(active_false)
print('-----')
print('-----')


# active_true = active_test.count('true')
# active_false = active_test.count('false')
