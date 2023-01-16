import json
import re

rides = json.loads(input())

properties = {
    'stop_name': {
        'regex': r'[A-Z].+ (Road|Avenue|Boulevard|Street)$',
    },
    'stop_type': {
        'regex': '[SOF]{,1}$'
    },
    'a_time': {
        'regex': '(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
    }
}

errors = {propKey: 0 for propKey in properties}

for ride in rides:
    for propKey in ride:
        if propKey in properties:
            val = ride[propKey]
            rules = properties[propKey]

            ruleRegex = rules.get('regex')

            is_invalid = ruleRegex and re.match(ruleRegex, val) is None

            if is_invalid:
                errors[propKey] += 1

errorsNum = sum(errors.values())
print(f'Type and required field validation: {errorsNum} errors')
for errKey in errors:
    errorNum = errors[errKey]
    print(f'{errKey}: {str(errorNum)}')
