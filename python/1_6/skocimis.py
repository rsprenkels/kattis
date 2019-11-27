# https://open.kattis.com/problems/skocimis

def skocimis(a, b, c):
    max_moves = max(b - a, c - b) - 1
    return max_moves


def test_1():
    assert skocimis(2, 3, 5) == 1


def test_2():
    assert skocimis(3, 5, 9) == 3


if __name__ == '__main__':
    print(skocimis(*list(map(int, input().split()))))
