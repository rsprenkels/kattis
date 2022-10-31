# https://open.kattis.com/problems/forcedchoice
from typing import List

def solution(N: int, P: int, takes: List[int]) -> str:
    results = []
    for take in takes:
        if P in take:
            results.append('KEEP')
        else:
            results.append('REMOVE')
    return results

def test_1():
    assert solution(10, 3, [[1,5],[2,3,7,8,10],[2,7,10],[8]]) == ['REMOVE','KEEP','REMOVE','REMOVE']

if __name__ == '__main__':
    N,P,S = map(int, input().split())
    takes = []
    for _ in range(S):
        takes.append(list(map(int, input().split()))[1:])
    print('\n'.join(solution(N, P, takes)))
