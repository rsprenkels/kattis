# https://open.kattis.com/problems/soylent
import math


def soylent(tot_calories):
    return math.ceil(tot_calories / 400)


def test_1():
    assert soylent(2000) == 5


def test_2():
    assert soylent(1600) == 4


if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        print(soylent(int(input())))
