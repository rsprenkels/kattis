# https://open.kattis.com/problems/register
import math
from typing import List

def solution(registers: List[int]) -> int:
    reg_size = [2,3,5,7,11,13,17,19]
    incs_possible = 0
    for ndx in range(len(registers)):
        cur_incs_possible = reg_size[ndx] - 1 - registers[ndx]
        if ndx > 0:
            multiplier = math.prod(reg_size[n] for n in range(ndx))
            cur_incs_possible *= multiplier
        incs_possible += cur_incs_possible
    return incs_possible

def test_1():
    assert solution(list(map(int, '0 0 4 6 10 12 16 18'.split()))) == 5

def test_2():
    assert solution(list(map(int, '1 2 4 6 10 12 16 18'.split()))) == 0

def test_3():
    assert solution(list(map(int, '0 0 0 0 0 0 0 0'.split()))) == 9699689

if __name__ == '__main__':
    registers = list(map(int, input().split()))
    result = solution(registers)
    print(result)