# https://open.kattis.com/problems/rectanglearea
from typing import List


def solution(r: List[float]) -> float:
    x1, y1, x2, y2 = r
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return w * h

# def test_1():
#     assert solution([0.0, 0.0, 3.0, 4.0]) == 12.000
#
# def test_2():
#     assert solution([5.2, -4.64, -3.47, 2.2]) == 59.303

if __name__ == '__main__':
    print(solution(list(map(float, input().split(' ')))))

