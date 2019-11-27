# https://open.kattis.com/problems/parking

def parking(prices, events):
    prices.insert(0, 0)
    trucks = [0 for _ in range(100)]
    for event in events:
        for minute in range(event[0], event[1]):
            trucks[minute] += 1
    total_due = sum([prices[trucks[minute]] * trucks[minute] for minute in range(100)])
    return total_due

def test_1():
    prices = [5, 3, 1]
    events = [(1, 6), (3, 5), (2, 8)]
    assert parking(prices, events) == 33

def test_2():
    prices = [10, 8, 6]
    events = [(15, 30), (25, 50), (70, 80)]
    assert parking(prices, events) == 480

if __name__ == '__main__':
    prices = list(map(int, input().split()))
    events = []
    for _ in range(3):
        events.append(tuple(map(int, input().split())))
    print(parking(prices, events))