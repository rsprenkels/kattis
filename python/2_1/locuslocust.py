# https://open.kattis.com/problems/locustlocus
from typing import List


def lcm(a, b):
    greater = max(a,b)
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def solution(pcs: List[List[int]]) -> int:
    first_pair = None
    for year, p1, p2 in pcs:
        pair_at = year + lcm(p1, p2)
        if first_pair == None or pair_at < first_pair:
            first_pair = pair_at
    return first_pair


def test_1():
    assert solution([[1192,13,17],[1992,14,18],[2001,5,7]]) == 2036

def test_2():
    assert solution([[2020,2,3],[2019,3,4]]) == 2026


if __name__ == '__main__':
    num_pairs = int(input())
    pairs = []
    for _ in range(num_pairs):
        pairs.append(list(map(int, input().split(' '))))
    print(solution(pairs))