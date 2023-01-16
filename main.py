import json

rides = json.loads(input())

wrong_buses = []

print('Arrival time test:')

for rideI, ride in enumerate(rides):
    prev_ride = rides[rideI - 1] if rideI > 0 else None

    is_invalid = ride['stop_type'] != 'S' and prev_ride['bus_id'] == ride['bus_id'] and \
                 ride['bus_id'] not in wrong_buses and prev_ride['a_time'] >= ride['a_time']

    if is_invalid:
        print(f"bus_id line {ride['bus_id']}: wrong time on station {ride['stop_name']}")
        wrong_buses.append(ride['bus_id'])

if len(wrong_buses) == 0:
    print('OK')
