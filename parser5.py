import json
import sys

with open('production.json') as file:
    data = json.load(file)

json_str = json.dumps(data)
resp = json.loads(json_str)

active_true = 'true number'
active_false = 'false number'

# GET ALL REGION CODES AND ACTIVE STATUS
print('region code, is active')
print('-----')
for key in resp:
    region = key
    status = (resp[region]['general']['active'])
    active_test = 'active' if status == True else 'non-active'
    print (region, status, active_test)

    # active_true = sum(1 for status in resp if True)
    # active_false = sum(1 for status in resp if False)

    # active = active_test.count('active')
    # non-active = active_test.count('non-active')
    # active_true = sum(1 if True else 0 for status in resp)
    # print active_true
print('-----')


# CLASSIFICATION OF REGIONS AS ACTIVE OR NON-ACTIVE

active_test_results = (for key in resp:
    region = key
    status = (resp[region]['general']['active'])
    active_test = 'active' if status == True else 'non-active'
)

active_true = sum(1 if 'active' else 0 for active_test in active_test_results)
# active_true = sum(1 for status in resp if True)
active_false = sum(1 for status in resp if False)


    # active = active_test.count('active')
    # non-active = active_test.count('non-active')
    # print(active)

# for (resp[key]['general']['active']) in resp:
#     active_true = 'active' + str(active_test.count('active'))
#     active_false = 'non-active' + str(active_test.count('non-active'))
# active_true = active_true.count('1')


# active_true = sum(1 for (resp[key]['general']['active']) in resp if True)
# active_false = sum(1 for (resp[key]['general']['active']) in resp if False)

# region = key
# status = (resp[key]['general']['active'])
# print status
# active_true = sum(1 if 'true' else 0 for status in resp)



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
