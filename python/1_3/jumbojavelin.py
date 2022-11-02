from typing import List, Tuple

def solution(rods: List[int]) -> int:
    return sum(rods) - len(rods) + 1

def test_1():
    assert solution([21, 34, 18, 9]) == 79

if __name__ == '__main__':
    num_rods = int(input())
    rods = []
    for _ in range (num_rods):
        rods.append(int(input()))
    print(solution(rods))