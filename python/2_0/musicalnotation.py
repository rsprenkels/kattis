# https://open.kattis.com/problems/musicalnotation
from typing import List


def solution (notes: str) -> List[str]:
    scale =     'abcdefgABCDEFG'
    empty_col = '-   - - - - - '
    row_numbers = {k:v for k,v in zip(list(scale), range(14))}
    rows = [[] for _ in range(len(row_numbers))]
    for ndx in range(len(rows)):
        rows[ndx].append(scale[ndx])
        rows[ndx].append(':')
        rows[ndx].append(' ')
    for ndx, note in enumerate(notes.split(' ')):
        col = list(empty_col)
        col[row_numbers[note[0]]] = '*'
        reps = 1 if len(note) == 1 else int(note[1:])
        for duration in range(reps):
            for dur_ndx, c in enumerate(col):
                rows[dur_ndx].append(c)
        for ndx, c in enumerate(empty_col):
            rows[ndx].append(c)

    res = []
    for r in reversed(rows):
        res.append(''.join(r[:-1]))
    return res


def test_1():
    assert solution('C C D E C E D2 C C D E C2 B2 C C D E F E D C B g A B C2 C2') ==\
"""
G:
F: -------------------------------------*--------------------
E:       *   *          *             *   *
D: ----*-------**-----*-------------*-------*----------------
C: * *     *      * *     **    * *           *         ** **
B: --------------------------**-----------------*-----*------
A:                                                  *
g: -----------------------------------------------*----------
f:
e: ----------------------------------------------------------
d:
c:
b:
a: ----------------------------------------------------------
"""

if __name__ == '__main__':
    _ = input()
    print('\n'.join(solution(input())))