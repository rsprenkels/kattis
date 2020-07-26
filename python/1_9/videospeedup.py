from typing import Sequence


def speedup(percentage: int, shorter_length: int, events: Sequence[int]) -> float:
    speed = 100
    orig_duration = 0
    events = [0] + events + [shorter_length]
    for ndx in range(len(events) - 1):
        orig_duration += (events[ndx + 1] - events[ndx]) * speed / 100.0
        speed += percentage
    return orig_duration

def test_1():
    assert speedup(percentage=20, shorter_length=15, events=[3, 10]) == 18.400

if __name__ == '__main__':
    n, p, k = map(int, input().split())
    events = list(map(int, input().split()))
    print(speedup(p, k, events))

# from 452.9 rank 802 to 454.8 rank 798
