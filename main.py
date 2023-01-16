import json

# constants
stops = ['road', 'avenue', 'boulevard', 'street', 'st.', 'av.', 'str.', 'road']

stop_types = ['S', 'O', 'F']

# validation groups constants
simple_int_fields = ['bus_id', 'stop_id', 'next_stop']
simple_time_fields = ['a_time']

# validation
data = json.loads(input())

errors = {
    'bus_id': 0,
    'stop_id': 0,
    'stop_name': 0,
    'next_stop': 0,
    'stop_type': 0,
    'a_time': 0
}

for ride in data:
    for fieldKey in ride:
        fieldVal = ride[fieldKey]

        isValid = True

        if fieldKey in simple_int_fields:
            isValid = type(fieldVal) is int
        elif fieldKey in simple_time_fields:
            if type(fieldVal) is not str:
                isValid = False
            else:
                timeArr = fieldVal.split(':')
                isValid = len(timeArr) == 2 \
                          and len(timeArr[0]) == 2 \
                          and len(timeArr[1]) == 2 \
                          and timeArr[0].isdigit() \
                          and timeArr[1].isdigit()
        elif fieldKey == 'stop_name':
            if type(fieldVal) is not str:
                isValid = False
            else:
                stopName = fieldVal.split()
                isValid = type(fieldVal) is str and fieldVal != ''
        elif fieldKey == 'stop_type':
            isValid = type(fieldVal) is str and (fieldVal == '' or fieldVal in stop_types)

        if isValid is False:
            errors[fieldKey] += 1

errorsNum = sum(errors.values())
print(f'Type and required field validation: {errorsNum} errors')
for errKey in errors:
    print(f'{errKey}: {str(errors[errKey])}')
