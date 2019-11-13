# https://open.kattis.com/problems/differentdistances
import math


def diffdist(x1, y1, x2, y2, p):
    result = math.pow(math.pow(abs(x1 - x2), p) + math.pow(abs(y1 - y2), p), 1.0 / p)
    return result


def test_diffdist():
    assert diffdist(*[1.0, 1.0, 2.0, 2.0, 2.0]) - 1.4142135624 <= 0.0001

def test_2():
    assert diffdist(*[1.0, 1.0, 20.0, 20.0, 10.0]) - 20.3636957882 <= 0.0001

if __name__ == '__main__':
    while True:
        line = input()
        if line == '0':
            exit()
        print(diffdist(*list(map(float, line.split()))))