import math
from typing import Tuple


def has_right_angle(sides: Tuple[int, int, int]) -> bool:
    s = sorted(sides)
    return pow(s[0], 2) + pow(s[1], 2) == pow(s[2], 2)

def test_1():
    assert has_right_angle((6, 8, 10)) == True
    assert has_right_angle((8, 6, 10)) == True
    assert has_right_angle((10, 6, 8)) == True
    assert has_right_angle((25, 52, 60)) == False

if __name__ == '__main__':
    while True:
        sides = list(map(int, input().split()))
        if all([s == 0 for s in sides]):
            break
        print('right' if has_right_angle(sides) else 'wrong')

# from 447.2 rank 810 to 449.0 rank 806

