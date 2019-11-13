# https://open.kattis.com/problems/freefood
from collections import defaultdict


def freefood(events):
    food_days = defaultdict(int)
    for event in events:
        start, end = event
        for day in range(start, end + 1):
            food_days[day] += 1
    return len(food_days)


def test_freefood():
    assert freefood([(10,14), (13,17), (25,26)]) == 10

def test_2():
    assert freefood([(1, 365), (20,28)]) == 365

if __name__ == '__main__':
    num_events = int(input())
    events = []
    for _ in range(num_events):
        events.append(tuple(map(int, input().split())))
    print(freefood(events))