import json

rides = json.loads(input())


def count_demand(stop_id):
    total = 0
    for ride in rides:
        if ride['next_stop'] == stop_id:
            total += 1
    return total


def main():
    print('On demand stops test:')

    demands = []

    for ride in rides:
        if ride['stop_type'] == 'O':
            demand_num = count_demand(ride['stop_id'])

            if demand_num > 1 and ride['stop_name'] not in demands:
                demands.append(ride['stop_name'])

    if demands:
        print('Wrong stop type:', sorted(demands))
    else:
        print('OK')


main()
