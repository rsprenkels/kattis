from typing import List

def solution(percentage: int) -> List[float]:
    return [100.0 / percentage, 100.0 / (100 - percentage)]

def test_1():
    assert solution(80) == [1.25, 5.0]

if __name__ == '__main__':
    percentage = int(input())
    result = solution(percentage)
    for p in result:
        print(f'{p}')