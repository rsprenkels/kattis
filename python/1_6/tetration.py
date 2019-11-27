# https://open.kattis.com/problems/tetration
import math


def tetration(N):
    amin = 1 / math.e
    amax = math.e

    for _ in range(20):
        mid = (amin + amax) / 2.0
        print(f"mid {mid}")
        res = f(mid, 200)
        if abs(res - N) < 0.000001:
            return
        if res < N:
            amin = mid
        else:
            amax = mid
    # print(f"a {N} amin {amin}")
    return amin


def test_1():
    result = tetration(2.000000) - 1.414214
    print(f"\nresult {result}")
    assert abs(result) <= 0.00001


def f(a, k):
    if k == 1:
        return a
    else:
        return pow(a, f(a, k - 1))


def test_2():
    a = 1.414214
    a = 1.5
    res = f(a, 500)
    print(f"\ncheckres {res} should be 2.000000")
