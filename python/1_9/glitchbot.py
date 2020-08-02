import copy
from typing import Sequence, Tuple


def final_location(instructions: Sequence[str]):
    x, y = 0, 0
    dir_x, dir_y = 0, 1
    for inst in instructions:
        if inst == 'Forward':
            x += dir_x
            y += dir_y
        elif inst == 'Right':
            dir_x, dir_y = dir_y, -dir_x
        else:
            dir_x, dir_y = -dir_y, dir_x
    return (x, y)


def glitchbot(x: int, y: int, instructions: Sequence[str]) -> Tuple[int, str]:
    for ndx, instruction in enumerate(instructions):
        for alt_inst in [a for a in ['Forward', 'Left', 'Right'] if a != instruction]:
            new_set = copy.deepcopy(instructions)
            new_set[ndx] = alt_inst
            if final_location(new_set) == (x, y):
                return (ndx + 1, alt_inst)
    return (99, 'error')

def test_1():
    assert glitchbot(3, 2, ['Forward','Right','Forward','Forward','Left','Forward','Forward','Left','Forward','Right','Forward',]) == (8, 'Right')

if __name__ == '__main__':
    x, y = map(int, input().split())
    instructions = []
    for _ in range(int(input())):
        instructions.append(input())
    result = glitchbot(x, y, instructions)
    print(f'{result[0]} {result[1]}')