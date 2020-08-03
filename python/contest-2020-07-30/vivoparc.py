import sys
from collections import defaultdict
from typing import Sequence, DefaultDict, Set

# needed a peek on https://github.com/mpfeifer1/Kattis/blob/master/vivoparc.cpp for algorithm

def solve(n: int, sees: Sequence[DefaultDict[int, Set]], animals: Sequence[int]) -> Sequence[int]:
    if n > len(animals):
        yield animals
    else:
        for animal in range(1, 5):
            still_okay = True
            for look_back_at in sees[n]:
                if look_back_at >= n:
                    continue
                if animals[look_back_at - 1] == animal:
                    still_okay = False
                    break
            if still_okay:
                animals[n - 1] = animal
                yield from solve(n + 1, sees, animals)

def vivoparc_elimination(n: int, restrictions, animals):
    sees = defaultdict(set)
    for r in restrictions:
        sees[r[0]].add(r[1])
        sees[r[1]].add(r[0])
    return next(solve(1, sees, animals))

def test_2():
    n = 8
    animals = [0] * n
    restrictions = [tuple(map(int, s.split('-'))) for s in """
1-2
3-1
4-5
4-8
1-7
1-4
7-1
2-4
1-8
6-7
2-3
1-5
1-6
7-6
7-8
2-5
7-1
3-4
5-6
7-8
"""[1:-1].split('\n')]
    assert vivoparc_elimination(n, restrictions, animals) == [1, 2, 3, 4, 3, 2, 3, 2]

def test_1():
    n = 8
    animals = [0] * n
    restrictions = []
    assert vivoparc_elimination(n, restrictions, animals) == [1, 1, 1, 1, 1, 1, 1, 1]

if __name__ == '__main__':
    n = int(input())
    animals = [0] * n
    restrictions = []
    for line in sys.stdin:
        restrictions.append(tuple(map(int, line.split('-'))))
    for ndx, v in enumerate(vivoparc_elimination(n, restrictions, animals), start=1):
        print(f'{ndx} {v}')
