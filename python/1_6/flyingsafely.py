# https://open.kattis.com/problems/flyingsafely
from collections import defaultdict

def flyingsafely(cities, schedule):
    return cities - 1

def test_1():
    assert flyingsafely(cities=3, schedule=[(1, 2), (2, 3), (1, 3), ]) == 2


def test_2():
    assert flyingsafely(cities=5, schedule=[(2, 1), (2, 3), (4, 3), (4, 5), ]) == 4


if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        cities, pilots = list(map(int, input().split()))
        for _ in range(pilots):
            a, b = list(map(int, input().split()))
        print(cities - 1)
