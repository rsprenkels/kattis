# https://open.kattis.com/problems/fodelsedagsmemorisering
from typing import List


def solution(lines: List[str]) -> List[str]:
    bd = dict()
    for line in lines:
        name, like, bday = line.split(' ')
        if bday not in bd.keys() or int(bd[bday][1]) < int(like):
            bd[bday] = (name, like)
    return sorted([bd[k][0] for k in bd.keys()])


def test_1():
    lines = """\
Sanna 1 16/03
Simon 2 16/03
Saga 3 14/10""".splitlines()
    assert solution(lines) == """\
Saga
Simon""".splitlines()

if __name__ == '__main__':
    n = int(input())
    bd = []
    for n in range(n):
        bd.append(input())
    s = solution(bd)
    print(len(s))
    print('\n'.join(s))