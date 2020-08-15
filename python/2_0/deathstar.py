from typing import Sequence


def deathstar(matrix: Sequence[Sequence[int]]) -> Sequence[int]:
    result = [0] * len(matrix)
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            result[row] |= matrix[row][col]
            result[col] |= matrix[row][col]
    return result


def test_1():
    raw_data = """
0 0 1 1 1
0 0 2 0 2
1 2 0 1 3
1 0 1 0 1
1 2 3 1 0
"""[1:-1].split('\n')
    matrix = [[int(x) for x in line.split()] for line in raw_data]
    assert deathstar(matrix) == [1, 2, 3, 1, 11]

if __name__ == '__main__':
    dim = int(input())
    matrix = []
    for _ in range(dim):
        matrix.append(list(map(int, input().split())))
    for r in deathstar(matrix):
        print(f'{r} ', end='')

# from 515.9 rank 682 (team 284.7 rank 132)
