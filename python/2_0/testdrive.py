import math

def solution(a,b,c) -> str:
    sign = lambda x: math.copysign(1, x)
    d1, d2 = b-a, c-b
    if d1 == d2:
        return 'cruised'
    elif abs(d1) < abs(d2) and sign(d1) == sign(d2):
        return 'accelerated'
    elif abs(d1) > abs(d2) and sign(d1) ==sign(d2):
        return 'braked'
    else:
        return 'turned'


def test_1():
    assert solution(1,2,3) == 'cruised'
    assert solution(5,4,1) == 'accelerated'
    assert solution(8,9,7) == 'turned'
    assert solution(10,20,25) == 'braked'


if __name__ == '__main__':
    print(solution(*list(map(int, input().split(' ')))))