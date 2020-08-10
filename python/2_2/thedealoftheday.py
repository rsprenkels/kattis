import functools
import itertools
import operator
from typing import Sequence


def the_deal_of_the_day(deck: Sequence[int], hand_size: int) -> int:
    candidates = [c for c in deck if c > 0]
    combinations = itertools.combinations(candidates, hand_size)
    total_strict_ascending = 0
    for comb in combinations:
        prod = functools.reduce(operator.mul, comb)
        total_strict_ascending += prod
    return total_strict_ascending

def test_1():
    assert the_deal_of_the_day([4, 0, 0, 0, 4, 0, 0, 0, 0, 4, ], 3) == 64


def test_2():
    assert the_deal_of_the_day([10, 10, 10, 20, 0, 10, 10, 10, 10, 10, ], 4) == 1820000

if __name__ == '__main__':
    deck = list(map(int, input().split()))
    hand_size = int(input())
    print(the_deal_of_the_day(deck=deck, hand_size=hand_size))

# from 502.3 rank 700
