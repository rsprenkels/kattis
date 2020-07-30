import sys
import timeit
from collections import defaultdict
from typing import Sequence, Tuple, Set


def g2(n, sees, sofar = None):
    if sofar == None:
        sofar = {}
    if n > 1:
        nxt = len(sofar) + 1
        nxt_seen_by = [k for k in sees if nxt in sees[k]]
        d = [sofar[k] for k in nxt_seen_by if k in sofar]
        opts = [x for x in range(1, 5) if x not in d]
        for x in opts:
            yield from g2(n - 1, sees, {**sofar,  **{len(sofar) + 1 : x}})
    else:
        nxt = len(sofar) + 1
        nxt_seen_by = [k for k in sees if nxt in sees[k]]
        d = [sofar[k] for k in nxt_seen_by if k in sofar]
        opts = [x for x in range(1, 5) if x not in d]
        for x in opts:
            yield list({**sofar,  **{len(sofar) + 1 : x}}.values())

def vivoparc(n: int, restrictions: Sequence[Tuple[int, int]]) -> Sequence[int]:
    sees = defaultdict(set)
    for r in restrictions:
        sees[r[0]].add(r[1])
        sees[r[1]].add(r[0])
    return next(g2(n, sees))

def test_1():
    n = 8
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
    assert vivoparc(n, restrictions) == [1,2,3,4,3,2,3,2]

if __name__ == '__main__':
    n = int(input())
    restrictions = []
    for line in sys.stdin:
        restrictions.append(tuple(map(int, line.split('-'))))
    for ndx, v in enumerate(vivoparc(n, restrictions), start=1):
        print(f'{ndx} {v}')
