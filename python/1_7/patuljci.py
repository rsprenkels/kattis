from itertools import combinations

from typing import Sequence

def dwarves(hatnumbers: Sequence[int]) -> Sequence[int]:
    for p in combinations(hatnumbers, 7):
        if sum(p) == 100:
            return list(p)

def test_dwarves1():
    assert dwarves([7, 8, 10, 13, 15, 19, 20, 23, 25]) == [7, 8, 10, 13, 19, 20, 23]

if __name__ == '__main__':
    hats = []
    for _ in range(9):
        hats.append(int(input()))
    for hat in dwarves(hats):
        print(hat)

# from 409.7 rank 908 to 411.4 rank 904
