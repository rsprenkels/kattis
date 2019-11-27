# https://open.kattis.com/problems/sodaslurper

def sodaslurper(e, f, c):
    full_bottles = 0
    empty = e + f
    while empty >= c:
        buy = empty // c
        empty -= buy * c
        full_bottles += buy
        empty += buy
    return full_bottles


def test_1():
    assert sodaslurper(9, 0, 3) == 4


def test_2():
    assert sodaslurper(5, 5, 2) == 9


if __name__ == '__main__':
    print(sodaslurper(*list(map(int, input().split()))))
