from typing import Sequence, Tuple


def cookingwater(not_look_ranges: Sequence[Tuple[int, int]]) -> bool:
    return min([t[1] for t in not_look_ranges]) < max([t[0] for t in not_look_ranges])

def test_1():
    assert cookingwater([(1,7),(5,5)]) == False

def test_2():
    assert cookingwater([(4,6),(4,8),(7,8)]) == True

if __name__ == '__main__':
    not_look_ranges = []
    for _ in range(int(input())):
        not_look_ranges.append(tuple(map(int, input().split())))
    if cookingwater(not_look_ranges):
        print('edward is right')
    else:
        print('gunilla has a point')

# from 438.5 rank 832 to 440.0 rank 831
