# https://open.kattis.com/contests/hsc8sj/problems/climbingworm
from math import ceil


def climbingworm(a, b, h):
    if a >= h:
        return 1
    else:
        return 1 + ceil((h - a) / (a - b))


def test_w1():
    assert climbingworm(5, 0, 15) == 3


def test_w2():
    assert climbingworm(3, 1, 4) == 2


if __name__ == '__main__':
    a, b, h = list(map(int, input().split()))
    print(climbingworm(a, b, h))
