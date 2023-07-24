from typing import List


def solution(numbers: List[int], k: int) -> List[int]:
    return [numbers[ndx] for ndx in range(k-1, len(numbers), k)]


def test_1():
    assert solution([1,2,3,4,5,6,7,8,9,10], 2) == [2,4,6,8,10]



if __name__ == '__main__':
    _, k = list(map(int, input().split(' ')))
    numbers = list(map(int, input().split(' ')))
    print(' '.join(map(str, solution(numbers, k))))