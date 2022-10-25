from typing import List


def solution(numbers: List[int]) -> str:
    for k in range(1, len(numbers)):
        # print(f'trying {k} on {numbers}')
        strict_increase = True
        range_length = 1
        for a, b in zip(range(k-1, len(numbers), k), range(2*k-1, len(numbers), k)):
            # print(f'comparing {a} {b}  values {numbers[a]} {numbers[b]}  {numbers}')
            if numbers[b] <= numbers[a]:
                strict_increase = False
                break
            else:
                range_length += 1
        if strict_increase and range_length >= 2:
            # print(f'for k {k} is range_len {range_length}')
            return f'{k}'
    return 'ABORT!'

def test_1():
    assert solution(list(map(int, '1 2 3 4 5 6 7 8 9 10'.split()))) == '1'


def test_2():
    assert solution(list(map(int, '1 8 2 7 3 6 4 5'.split()))) == '3'


def test_3():
    assert solution(list(map(int, '9 8 8 4 4 3 10 1 1 0'.split()))) == 'ABORT!'


if __name__ == '__main__':
    input()
    numbers = list(map(int, input().split()))
    result = solution(numbers)
    print(result)
