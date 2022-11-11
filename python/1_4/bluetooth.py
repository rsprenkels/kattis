# https://open.kattis.com/problems/bluetooth
from typing import List


def solution (bad_teeth: List[str]) -> int:
    teeth = [[{1,2,3,4,5,6,7,8},{1,2,3,4,5,6,7,8}],[{1,2,3,4,5,6,7,8},{1,2,3,4,5,6,7,8}]]
    side_no_blue_tooth = [True, True]

    tooth = 0
    for t in bad_teeth:
        is_right = 1 if t[0].isdigit() else 0
        if is_right == 1:
            tooth = int(t[0])
            is_upper = 1 if t[1] == '+' else 0
        else:
            tooth = int(t[1])
            is_upper = 1 if t[0] == '+' else 0
        if t[3] == 'b':
            side_no_blue_tooth[is_right] = False
        else:
            teeth[is_upper][is_right].remove(tooth)

    if side_no_blue_tooth[0] and len(teeth[0][0]) > 0 and len(teeth[1][0]) > 0:
        return 0
    elif side_no_blue_tooth[1] and len(teeth[0][1]) > 0 and len(teeth[1][1]) > 0:
        return 1
    else:
        return 2

def test_1():
    assert solution(['-5 b']) == 1

def test_2():
    teeth = [
        '8- m',
        '7- m',
        '6- m',
        '5- m',
        '4- m',
        '3- m',
        '2- m',
        '1- m',
        '+3 b', ]
    assert solution(teeth) == 2

if __name__ == '__main__':
    teeth = []
    for _ in range(int(input())):
        teeth.append(input())
    print(solution(teeth))