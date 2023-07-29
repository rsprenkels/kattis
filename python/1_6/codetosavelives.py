# https://open.kattis.com/problems/codetosavelives
from typing import List


def solution(nums: List[str]) -> List[str]:
    res = []
    for tc in range(0,len(nums), 2):
        d1 = int(nums[tc].replace(' ',''))
        d2 = int(nums[tc+1].replace(' ',''))
        res.append(' '.join(list(str(d1+d2))))
    return res

def test_1():
    input_lines = """\
3 4 5
5 6 7
6 1
3 2 5""".splitlines()
    assert solution(input_lines) == """\
9 1 2
3 8 6""".splitlines()


if __name__ == '__main__':
    nums = []
    tc = int(input())
    for _ in range(tc*2):
        nums.append(input())
    print('\n'.join(solution(nums)))