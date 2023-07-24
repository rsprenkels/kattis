# https://open.kattis.com/problems/monopol
from itertools import product
from typing import List


def solution(hotels: List[int]) -> float:
    def p(x: int) -> float:
        return sum(1 for a,b in product([1,2,3,4,5,6], repeat=2) if a + b == x) / 36.0

    return sum(p(x) for x in hotels)


def test_1():
    assert solution([7]) == 0.16666666666666666


def test_2():
    assert solution([2, 12]) == 0.05555555555555555


if __name__ == '__main__':
    _ = input()
    hotels = list(map(int, input().split(' ')))
    print(solution(hotels))







