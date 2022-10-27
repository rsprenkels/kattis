# https://open.kattis.com/problems/janitortroubles
# needed google for the fomula.

import math

def solution(a: int, b: int, c:int, d:int) -> float:
    s = (a + b + c + d) / 2 # semi_perimeter

    return math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

def test_1():
    assert solution(3,3,3,3) == 9

def test_2():
    assert solution(1,2,1,1) == 1.299038105676658

if __name__ == '__main__':
    sides = list(map(int, input().split()))
    answer = solution(*sides)
    print(answer)