def hanging_out(max_load, events):
    current_load = 0
    groups_denied = 0
    for event in events:
        type, amount = event.split()
        amount = int(amount)
        if type == 'enter':
            if current_load + amount <= max_load:
                current_load += amount
            else:
                groups_denied += 1
        else:
            current_load -= amount
    return groups_denied



def test_hangingout():
    assert hanging_out(4, ['enter 3','enter 2','leave 1','enter 1','enter 2']) == 2


if __name__ == '__main__':
    max_load, num_events = list(map(int, input().split()))
    events = []
    for i in range(num_events):
        events.append(input())
    print(hanging_out(max_load, events))