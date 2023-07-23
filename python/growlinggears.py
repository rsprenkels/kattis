from typing import List, Tuple

def solution (gears: List[Tuple[int, int, int]]) -> int:
    max_torque_ndx = None
    max_torque = None
    for ndx, gear in enumerate(gears):
        a,b,c = gear
        # print(f'ndx:{ndx} {a} {b} {c}')
        R = b / (2 * a)  # max Torq at this RPM
        ndx_T = -a * (R ** 2) + b * R + c
        if max_torque == None or (R >= 0 and ndx_T > max_torque):
            max_torque_ndx = ndx
            max_torque = ndx_T
    return max_torque_ndx + 1

def test_1():
    assert solution([(1, 4, 2)]) == 1

def test_2():
    assert solution([(3, 126, 1400),(2, 152, 208)]) == 2

if __name__ == '__main__':
    num_testcases = int(input())
    for tc in range(num_testcases):
        num_gears = int(input())
        gears = []
        for _ in range(num_gears):
            gears.append(tuple(map(int, input().split())))
        print(solution(gears))