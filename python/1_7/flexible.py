from typing import Sequence
from itertools import combinations

def flexible(width: int, parts: Sequence[int]) -> Sequence[int]:
    parts.insert(0, 0)
    parts.append(width)
    possible = set()
    for pair in combinations(parts, 2):
        possible.add(abs(pair[1] - pair[0]))
    return sorted(possible)

def test_flexible():
    assert flexible(10, [1,4,8]) == [1,2,3,4,6,7,8,9,10]
    assert flexible(6, [2,5]) == [1,2,3,4,5,6]


if __name__ == '__main__':
    width, _ = map(int, input().split())
    parts = list(map(int, input().split()))
    print(' '.join(map(str, flexible(width, parts))))

# from 411.4 rank 904 to 413.1 rank 902
