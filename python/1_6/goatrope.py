import math
from typing import List


def solution(g: List[int]) -> float:
    x,y, x1, y1, x2, y2 = g
    if x <= x1:
        dx = x1-x
        if y <= y1:
            dy = y1-y
            return(math.sqrt(dx*dx + dy*dy))
        elif y >= y2:
            dy = y-y2
            return(math.sqrt(dx*dx + dy*dy))
        else:
            dy = 0
            return(math.sqrt(dx*dx + dy*dy))
    elif x >= x2:
        dx = x-x2
        if y <= y1:
            dy = y1-y
            return(math.sqrt(dx*dx + dy*dy))
        elif y >= y2:
            dy = y-y2
            return(math.sqrt(dx*dx + dy*dy))
        else:
            dy = 0
            return(math.sqrt(dx*dx + dy*dy))
    else:
        dx=0
        if y <= y1:
            dy = y1-y
            return(math.sqrt(dx*dx + dy*dy))
        elif y >= y2:
            dy = y-y2
            return(math.sqrt(dx*dx + dy*dy))
        else:
            dy = 0
            return(math.sqrt(dx*dx + dy*dy))


def test_1():
    assert solution([7,3,0,0,5,4]) == 2.0
    assert solution([6,0,0,2,7,6]) == 2.0
    assert solution([3,-4,-3,-1,-1,2]) == 5.0


if __name__ == '__main__':
    print(solution(list(map(int, input().split(' ')))))
