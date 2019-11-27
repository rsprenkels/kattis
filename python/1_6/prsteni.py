# https://open.kattis.com/problems/prsteni
import math


def simplyfy(n, d):
    candidates = range(d, 1, -1)
    for tst in candidates:
        if d % tst == 0 and n % tst == 0:
            return (n // tst, d // tst)
    return (n, d)


def prsteni(rings):
    first_ring = rings[0]
    output = []
    for ring in rings[1:]:
        n, d = simplyfy(first_ring, ring)
        output.append(f"{n}/{d}")
    return output

def test_1():
    assert prsteni([8, 4, 2]) == ['2/1', '4/1',]

def test_2():
    assert prsteni([12, 3, 8, 4]) == ['4/1', '3/2', '3/1',]

def test_3():
    assert prsteni([300, 1, 1, 300]) == ['300/1', '300/1', '1/1',]

if __name__ == '__main__':
    _ = input()
    rings = list(map(int, input().split()))
    for res in prsteni(rings):
        print(res)