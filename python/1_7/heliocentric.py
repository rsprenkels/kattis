import sys
from typing import Sequence, Tuple

def heliocentric(testcase: Tuple[int, int]) -> int:
    days = 0
    earth, mars = testcase
    while not (earth == 0 and mars == 0):
        add = 365 - earth
        earth = (earth + add) % 365
        mars = (mars + add) % 687
        days += add
    return days

def test_hc_1():
    assert heliocentric((0, 0)) == 0

def test_hc_2():
    assert heliocentric((364, 686)) == 1

def test_hc_3():
    assert heliocentric((360, 682)) == 5

def test_hc_4():
    assert heliocentric((0, 1)) == 239075

def test_hc_5():
    assert heliocentric((1, 0)) == 11679

if __name__ == '__main__':
    testcases = [tuple(map(int, line.split())) for line in sys.stdin]
    for ndx, tc in enumerate(testcases):
        print(f'Case {ndx + 1}: {heliocentric(tc)}')

# from 433.2 rank 843 to 434.9 rank 837
