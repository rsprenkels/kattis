from typing import List


def solution(n:int, k:int, ratings: List[int]) -> str:
    remaining_ratings = n - k
    return [(sum(ratings) - remaining_ratings * 3) / n,  (sum(ratings) + remaining_ratings * 3) / n]

def test_1():
    assert solution(5, 2, [1,2]) == [-1.2, 2.4]


if __name__ == '__main__':
    n, k  = map(int, input().split())
    ratings = []
    for _ in range(k):
        ratings.append(int(input()))
    result = solution(n, k, ratings)
    print(result[0], result[1])