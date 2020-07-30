from typing import Sequence, Tuple


def point_add(a: Tuple[int, int], b:Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])

def gold(map: Sequence[str]) -> int:
    gold_found = 0
    symbols = {}
    for row in range(len(map)):
        for col, symbol in enumerate(map[row]):
            symbols[(col, row)] = symbol
    player_loc = [loc for loc in symbols if symbols[loc] == 'P'][0]
    todo = [player_loc]
    seen = []
    while todo:
        location = todo.pop(0)
        seen.append(location)
        if symbols[location] == 'G':
            gold_found += 1
        if not any([symbols[point_add(location, around)] == 'T' for around in [(0, 1), (0, -1), (1, 0), (-1, 0)]]):
            for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                target = point_add(location, step)
                if target in symbols and symbols[target] in 'G.' and target not in seen and target not in todo:
                    todo.append(target)
    return gold_found

def test_1():
    map = """
########
#...GTG#
#..PG.G#
#...G#G#
#..TG.G#
########
"""[1:-1].split('\n')
    assert gold(map) == 4

if __name__ == '__main__':
    width, height = map(int, input().split())
    map = []
    for _ in range(height):
        map.append(input())
    print(gold(map))
