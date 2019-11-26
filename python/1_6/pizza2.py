# https://open.kattis.com/problems/pizza2
import math


def pizza2(radius, crust):
    return (math.pi * pow(radius - crust, 2)) / (math.pi * pow(radius, 2)) * 100.0


def test_1():
    assert pizza2(1, 1) == 0.00

def test_2():
    assert pizza2(2, 1) == 25.0000

if __name__ == '__main__':
    radius, crust = list(map(int, input().split()))
    print(pizza2(radius, crust))