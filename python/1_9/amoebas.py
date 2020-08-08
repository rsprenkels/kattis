from collections import defaultdict
from typing import Tuple, DefaultDict, List, Set, Dict


def amoebas(lines: List[str]) -> int:
    cells: Dict[Tuple[int, int], Set[Tuple[int, int]]] = dict()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                cells[(row, col)] = set()
    for cell in cells.keys():
        x, y = cell
        for dx, dy in [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]:
            if (x+dx, y+dy) in cells.keys():
                cells[cell].add((x+dx, y+dy))
    loops = 0
    todo: Set = set(cells.keys())
    while todo:
        loops += 1
        seen = set()
        Q = [todo.pop()]
        while Q:
            c = Q.pop()
            seen.add(c)
            Q.extend(cells[c] - seen)
        todo -= seen
    return loops

def test_1():
    lines = """
.##########.
#..........#
#..#...##..#
#.##..#..#.#
#......#.#.#
#....#..#..#
#...#.#....#
#..#...#...#
.#..#.#....#
#....#.....#
#.........#.
.#########..    
"""[1:-1].split('\n')

    assert amoebas(lines) == 4


if __name__ == '__main__':
    rows, cols = map(int, input().split())
    lines = []
    for _ in range(rows):
        lines.append(input())
    print(amoebas(lines))


# from 498.3 rank 709 to 500.2 rank 707