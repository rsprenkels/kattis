from typing import List

def solution(numbers: List[int]) -> List[int]:
    return list(reversed(numbers))

def test_1():
    numbers = list(map(int, '1 2 3 4 5 6 7 8 9 10'.split()))
    assert solution(numbers) == list(reversed(numbers))

if __name__ == '__main__':
    tot_numbers = int(input())
    numbers = []
    for n in range(tot_numbers):
        numbers.append(int(input()))
    result = solution(numbers)
    for n in result:
        print(n)
