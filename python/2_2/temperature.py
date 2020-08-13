from typing import Tuple


def temperature(x: int, y: int) -> Tuple[str, float]:
    if y == 1:
        if x == 0:
            return ('ALL GOOD', 0.0)
        else:
            return ('IMPOSSIBLE', 0.0)
    return ('normal', x / (1 - y))



def test_1():
    assert temperature(32, 2) == ('normal', -32)
    assert temperature(1, 3) == ('normal', -0.5)


def test_2():
    assert temperature(32, 1) == ('IMPOSSIBLE', 0)

def test_3():
    assert temperature(0, 1) == ('ALL GOOD', 0)


if __name__ == '__main__':
    res = temperature(*list(map(int, input().split())))
    if res[0] is not 'normal':
        print(res[0])
    else:
        print(res[1])

# from 509.4 rank 687 (team 283.0 rank 132)
