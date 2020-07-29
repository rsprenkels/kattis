from typing import Sequence


def lawnmower(width: float, lenght_mows: Sequence[float], width_mows: Sequence[float]) -> bool:
    halfwidth = width / 2.0
    length = [(s - halfwidth, s + halfwidth) for s in sorted(lenght_mows)]
    width = [(s - halfwidth, s + halfwidth) for s in sorted(width_mows)]
    if length[0][0] > 0 or length[-1][1] < 75:
        return False
    if width[0][0] > 0 or width[-1][1] < 100:
        return False
    if any([length[x][1] < length[x+1][0] for x in range(len(length) - 1)]):
        return False
    if any([width[x][1] < width[x+1][0] for x in range(len(width) - 1)]):
        return False
    return True

def test_1():
    assert lawnmower(10.0, [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0],
                     [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]) == True

def test_2():
    assert lawnmower(20.0, [60.0, 10.0, 30.0, 50.0], [30.0, 10.0, 90.0, 50.0, 70.0]) == False


if __name__ == '__main__':
    while True:
        _x, _y, width = map(float, input().split())
        if _x == 0 and _y == 0 and width == 0.0:
            break
        length_mows = list(map(float, input().split()))
        width_mows = list(map(float, input().split()))
        print(['NO', 'YES'][lawnmower(width, length_mows, width_mows)])

# from 462.6 rank 778 to 464.6 rank 774
