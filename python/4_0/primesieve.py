#  https://open.kattis.com/problems/primesieve
from typing import List

def solution(n: int, primes: List[int]) -> List[int]:
    def sieve(max_p):
        D = {}
        q = 2
        while q <= max_p:
            if q not in D:
                yield q
                D[q*q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p+q,[]).append(p)
                del D[q]
            q += 1

    tot_primes = 0
    all_primes = []
    for p in sieve(n):
        tot_primes += 1
    return [tot_primes]

    # all_primes = list(sieve(n))
    # print(sys.getsizeof(all_primes))
    # return [len(all_primes)] + [1 if p in all_primes else 0 for p in primes]


def solution_2(n: int, primes: List[int]) -> List[int]:
    def is_not_prime(sieve, x):
        return sieve[int(x / 64)] & (1 << ((x >> 1) & 31))

    def mark_not_prime(sieve, x):
        sieve[int(x / 64)] |= (1 << ((x >> 1) & 31))

    sieve = [0 for _ in range(int(n / 64) + 1)]
    for x in range(3, n + 1, 2):
        if x * x <= n:
            if is_not_prime(sieve, x):
                continue
            else:
                k = x << 1
                for j in range(x * x, n, k):
                    mark_not_prime(sieve, j)
    result = [sum([1 for x in range(1, n+1, 2) if not is_not_prime(sieve, x)])]
    for p in primes:
        if p == 2:
            result.append(1)
        elif p % 2 == 0 or p == 1:
            result.append(0)
        else:
            result.append(0 if is_not_prime(sieve, p) else 1)
    return result

# def test_1():
#     assert solution(9973,[1,2,3,4,9972,9973]) == [1229,0,1,1,0,0,1]

def test_2():
    assert solution(10**8,[1,2,3,4,9972,9973]) == [5761455,0,1,1,0,0,1]

if __name__ == '__main__':
    n, q = list(map(int, input().split()))
    numbers = []
    for _ in range(q):
        numbers.append(int(input()))
    result = solution(n, numbers)
    print('\n'.join([str(n) for n in result]))