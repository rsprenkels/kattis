from typing import List


def okvir(puzzle: List[str], U: int, L: int, R: int, D: int) -> List[str]:
    M, N = len(puzzle), len(puzzle[0])
    output = []
    for row in range(M + U + D):
        if row % 2 == 0:
            line = (['#', '.'] * (N + L + R))[:N + L + R]
        else:
            line = (['.', '#'] * (N + L + R))[:N + L + R]
        output.append(line)

    for y, row in enumerate(puzzle):
        for x, c in enumerate(row):
            output[y+U][x+L] = c

    result = []
    for row in output:
        result.append(''.join(row))
    return result

def test_1():
    puzzle = """
honi
oker
nera
irak
"""[1:-1].split('\n')
    output = """
#.#.#.#.
.#.#.#.#
#.honi#.
.#oker.#
#.nera#.
.#irak.#
#.#.#.#.
.#.#.#.#
"""[1:-1].split('\n')
    assert okvir(puzzle, 2, 2, 2, 2) == output

if __name__ == '__main__':
    N, M = map(int, input().split())
    U, L, R, D = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(input())
    for line in okvir(puzzle, U, L, R, D):
        print(line)

# from 527.5 rank 662 (team 287.2 rank 130)