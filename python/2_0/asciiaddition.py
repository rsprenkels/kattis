# https://open.kattis.com/problems/asciiaddition
from typing import List

symbols_def = \
"""xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx
....x
....x
....x
....x
....x
....x
....x
xxxxx
....x
....x
xxxxx
x....
x....
xxxxx
xxxxx
....x
....x
xxxxx
....x
....x
xxxxx
x...x
x...x
x...x
xxxxx
....x
....x
....x
xxxxx
x....
x....
xxxxx
....x
....x
xxxxx
xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx
xxxxx
....x
....x
....x
....x
....x
....x
xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx
xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx
.....
..x..
..x..
xxxxx
..x..
..x..
.....""".split('\n')

def solution(lines: List[str]) -> List[str]:
    s = []
    exp = []
    for y in range(0, len(symbols_def), 7):
        s.append(''.join(symbols_def[y:y+7]))
    sd = dict(zip(s,'0123456789+'))
    dig_to_asc = dict(zip('0123456789+', s))
    for topleft in range(0, len(lines[0]), 6):
        exp.append(sd[''.join(lines[y][topleft:topleft+5] for y in range(7))])
    result = eval(''.join(exp))
    reslines = ['' for _ in range(7)]
    for d in str(result):
        for row in range(7):
            reslines[row] += dig_to_asc[d][row*5:(row+1)*5] + '.'
    reslines = [line[:-1] for line in reslines]
    return reslines


def test_1():
    exp = \
"""\
....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx
....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x
....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx""".splitlines()

    expected_result = """\
....x.xxxxx.xxxxx.xxxxx.x...x.xxxxx.xxxxx
....x.....x.....x.x.....x...x.x.........x
....x.....x.....x.x.....x...x.x.........x
....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x
....x.x.........x.....x.....x.....x.....x
....x.x.........x.....x.....x.....x.....x
....x.xxxxx.xxxxx.xxxxx.....x.xxxxx.....x""".splitlines()
    assert solution(exp) == expected_result

if __name__ == '__main__':
    exp = []
    for _ in range(7):
        exp.append(input())
    print('\n'.join(solution(exp)))