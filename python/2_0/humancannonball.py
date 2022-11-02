from typing import List, Tuple

def solution(A: Tuple[float, float], B: Tuple[float, float], canons: List[Tuple[float, float]]) -> float:
    # need a shortest path algorithm here
    

def test_1():
    assert solution((25.0, 100.0), (190.0, 57.5), [(125.0, 67.5), (75.0, 125.0), (45.0, 72.5), (185.0, 102.5)]) == 19.984901

if __name__ == '__main__':
    A = tuple(map(float, input().split()))
    B = tuple(map(float, input().split()))
    num_canons = int(input())
    canons = []
    for _ in range(num_canons):
        canon = tuple(list(map(float, input().split())))
        canons.append(canon)
    print(solution(A, B, canons))