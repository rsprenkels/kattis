from typing import Sequence, Tuple

def dominos(num_tiles: int, vertices: Sequence[Tuple[int, int]]) -> int:
    knocks_over = dict()
    knocked_over_by = dict()
    for a, b in vertices:
        knocks_over[a] = b
        knocked_over_by[b] = a
    need_falling = {n for n in range(1, num_tiles + 1)}
    knocks_needed = 0
    while need_falling:
        knocks_needed += 1
        start_up = start_down = need_falling.pop()
        while start_up in knocked_over_by:
            start_up = knocked_over_by[start_up]
            need_falling.remove(start_up)
        while start_down in knocks_over:
            start_down = knocks_over[start_down]
            need_falling.remove(start_down)
    return knocks_needed

def test_1():
    assert dominos(3, [(1, 2), (2, 3)]) == 1

def test_2():
    assert dominos(6, [(4, 5), (2, 3), (1, 2), ]) == 3
    assert dominos(6, [(2, 3), (1, 2), ]) == 4
    assert dominos(6, [(2, 3), (1, 2), (4, 5), ]) == 3

def test_3():
    assert dominos(0, [ ]) == 0

def test_4():
    assert dominos(6, []) == 6

if __name__ == '__main__':
    for _ in range(int(input())):
        num_tiles, num_lines = map(int, input().split())
        vertices = []
        for _ in range(num_lines):
            vertices.append(tuple(map(int, input().split())))
        print(dominos(num_tiles, vertices))