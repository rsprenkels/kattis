from typing import Sequence

def solution(P: int, T: int, cases : Sequence[str]) -> int:
    tests_passed = 0
    for p in range(P):
        if all([tc[1:].lower() == tc[1:] for tc in cases[p*T:(p+1)*T]]):
            tests_passed += 1
    return tests_passed

def test_1():
    assert solution(2, 2, ['abc', 'Def', 'DDG', 'add']) == 1

if __name__ == '__main__':
    P, T = map(int, input().split())
    tc = []
    for _ in range(P * T):
        tc.append(input())
    print(solution(P, T, tc))

# from 421.4 rank 872 to 423.2 rank 867
