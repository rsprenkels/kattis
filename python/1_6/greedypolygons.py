# https://open.kattis.com/problems/greedypolygons
import math
from typing import List

def solution(cases: List[List[int]]) -> List[float]:
    result = []
    for tc in cases:
        n,b,d,g = tc
        ngon_area = (n*b*b*math.tan(math.radians(90 - 180/n)))/4
        ngon_area += n*b*d*g
        ngon_area += math.pi * pow(d*g, 2)
        result.append(ngon_area)
    return result


# def test_1():
#     assert solution([[3,8,1,1],[4,5,2,2]]) == pytest.approx([54.85440557469184, 155.2654824574367])


if __name__ == '__main__':
    n = int(input())
    tc = []
    for _ in range(n):
        tc.append(list(map(int, input().split(' '))))
    print('\n'.join(map(str, solution(tc))))

