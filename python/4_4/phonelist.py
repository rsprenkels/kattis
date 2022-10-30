from collections import defaultdict
from typing import List
from itertools import permutations

# def solution(numbers: List[str]) -> str:
#     for p in permutations(range(len(numbers)), 2):
#         if numbers[p[0]].startswith(numbers[p[1]]):
#             return 'NO'
#     return 'YES'

def solution(numbers: List[str]) -> str:
    per_len = defaultdict(list)
    for number in numbers:
        per_len[len(number)].append(number)
    num_lenghts = sorted(per_len.keys())
    # print(f'per_len:{per_len}  num_lengths:{num_lenghts}')
    for ndx, num_len in enumerate(num_lenghts):
        # print(f'ndx:{ndx} num_len:{num_len}')
        for short_num in per_len[num_len]:
            for rest in num_lenghts[ndx+1:]:
                for long_num in per_len[rest]:
                    if long_num.startswith(short_num):
                        return 'NO'
    return 'YES'

def test_1():
    assert solution(['911','97625999','91125426']) == 'NO'

def test_2():
    assert solution(['113','12340','123440','12345','98346']) == 'YES'

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        list_len = int(input())
        numbers = []
        for _ in range(list_len):
            numbers.append(input())
        print(solution(numbers))