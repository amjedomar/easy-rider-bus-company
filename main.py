import json
# import re

# input
rides = json.loads(input())

# validation
# properties = {
#     'stop_name': {
#         'regex': r'[A-Z].+ (Road|Avenue|Boulevard|Street)$',
#     },
#     'stop_type': {
#         'regex': '[SOF]{,1}$'
#     },
#     'a_time': {
#         'regex': '(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
#     }
# }
#
# errors = {propKey: 0 for propKey in properties}
#
# for ride in rides:
#     for propKey in ride:
#         if propKey in properties:
#             val = ride[propKey]
#             rules = properties[propKey]
#
#             ruleRegex = rules.get('regex')
#
#             is_invalid = ruleRegex and re.match(ruleRegex, val) is None
#
#             if is_invalid:
#                 errors[propKey] += 1
#
# errorsNum = sum(errors.values())
# print(f'Type and required field validation: {errorsNum} errors')
# for errKey in errors:
#     errorNum = errors[errKey]
#     print(f'{errKey}: {str(errorNum)}')

# stops
stops = {}

print('Line names and number of stops:')

for ride in rides:
    bus_id = ride['bus_id']
    stops[bus_id] = stops.get(bus_id, 0) + 1

for bus_id in stops:
    print(f"bus_id: {bus_id}, stops: {stops[bus_id]}")
