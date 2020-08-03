from typing import Sequence


def anotherbrick(height: int, width: int, bricks: Sequence[int]) -> bool:
    for layer in range(height):
        tot_width = 0
        while tot_width < width:
            tot_width += bricks.pop(0)
        if tot_width > width:
            return False
    return  True


def test_1():
    assert anotherbrick(height=2, width=10, bricks=[5, 5, 5, 5, 5, 5, 5]) == True


def test_2():
    assert anotherbrick(height=2, width=10, bricks=[5, 5, 5, 3, 5, 2, 2]) == False

if __name__ == '__main__':
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    if anotherbrick(h, w, bricks):
        print('YES')
    else:
        print('NO')

# from 454.8 rank 798 to
