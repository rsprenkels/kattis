# https://open.kattis.com/problems/cutthenegativity
from itertools import product
from typing import List, Tuple


def solution (city_matrix: List[List[int]]) -> List[List[int]]:
    num_cities = len(city_matrix[0])
    flights = []
    for y, x in product(range(num_cities), repeat=2):
        if city_matrix[y][x] != -1:
            flights.append([y+1, x+1, city_matrix[y][x]])
    return flights

def test_1():
    city_matrix = [
        [-1, 1, -1, 2],
        [9, -1, -1, -1],
        [-1, 3, -1, 4],
        [7, 1, 2, -1],
    ]
    result = solution(city_matrix)
    assert result == [
        [1,2,1],
        [1,4,2],
        [2,1,9],
        [3,2,3],
        [3,4,4],
        [4,1,7],
        [4,2,1],
        [4,3,2],]

if __name__ == '__main__':
    num_cities = int(input())
    city_matrix = []
    for _ in range(num_cities):
        city_matrix.append(list(map(int, input().split(' '))))
    result = solution(city_matrix)
    print(len(result))
    for row in result:
        print(' '.join(map(str, row)))