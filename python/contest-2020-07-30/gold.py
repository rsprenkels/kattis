from typing import Sequence


def gold(map: Sequence[str]) -> int:
    symbols = {}
    for row in range(len(map)):
        for col, symbol in enumerate(map[row]):
            symbols[(col, row)] = symbol
    player_loc = [loc for loc in symbols if symbols[loc] == 'P']
    safe_to_explore = [player_loc]
    visited = [player_loc]

def test_1():
    map = """
########
#...GTG#
#..PG.G#
#...G#G#
#..TG.G#
########
"""[1:-1].split('\n')
    assert gold(map) == 1