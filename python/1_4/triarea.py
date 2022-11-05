def solution(w: int, h:int) -> float:
    return w * h / 2.0

def test_1():
    assert solution(2,2) == 2

if __name__ == '__main__':
    print(solution(*list(map(int, input().split()))))