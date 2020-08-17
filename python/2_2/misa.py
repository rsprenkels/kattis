from typing import Sequence, Tuple, Set

def misa(church: Sequence[str]) -> int:
    pairs: Set[Tuple[int, int]] = set()
    w, h = len(church[0]), len(church)
    for row, seats in enumerate(church):
        for col, chair in enumerate(seats):
            if chair == 'o':
                for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                    x, y = col + dx, row + dy
                    if x >= 0 and x < w and y >= 0 and y < h:
                        if church[y][x] == 'o':
                            pairs.add(tuple(sorted([row * w + col, y * w + x])))
    start_handshakes = len(pairs)
    max_handshakes = start_handshakes
    for row, seats in enumerate(church):
        for col, chair in enumerate(seats):
            if chair == '.':
                extra_handshakes = 0
                for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                    x, y = col + dx, row + dy
                    if x >= 0 and x < w and y >= 0 and y < h:
                        if church[y][x] == 'o':
                            extra_handshakes += 1
                max_handshakes = max(max_handshakes, start_handshakes + extra_handshakes)
    return max_handshakes

def test_1():
    assert misa(['oo','oo']) == 6

def test_2():
    assert misa(['..o','o..']) == 2


if __name__ == '__main__':
    h, w = map(int, input().split())
    rows = []
    for _ in range(h):
        rows.append(input())
    print(misa(rows))

# from 521.5 rank 671 (team 286.0 rank 132)