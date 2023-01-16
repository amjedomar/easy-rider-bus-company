import json

rides = json.loads(input())

def has_stop(match_val, stop_type):
    for ride in rides:
        if ride['bus_id'] == match_val and ride['stop_type'] == stop_type:
            return True
    return False


def stop_count(stop_name):
    count = 0
    for ride in rides:
        if ride['stop_name'] == stop_name:
            count += 1
    return count


def main():
    starts, transfers, finishes = [[] for _ in range(0, 3)]

    for ride in rides:
        bus_id = ride['bus_id']
        stop_type = ride['stop_type']
        stop_name = ride['stop_name']

        if stop_type == 'S' and stop_name not in starts:
            if not has_stop(bus_id, 'F'):
                return print(f'There is no start or end stop for the line: {bus_id}.')
            starts.append(stop_name)
        elif stop_type == 'F' and stop_name not in finishes:
            if not has_stop(bus_id, 'S'):
                return print(f'There is no start or end stop for the line: {bus_id}.')
            finishes.append(stop_name)
        elif stop_name not in transfers and stop_count(stop_name) > 1:
            transfers.append(stop_name)

    print('Start stops:', len(starts), sorted(starts))
    print('Transfer stops:', len(transfers), sorted(transfers))
    print('Finish stops:', len(finishes), sorted(finishes))


main()
