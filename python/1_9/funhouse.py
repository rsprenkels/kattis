from typing import List

dir_left = (-1, 0)
dir_right = (1, 0)
dir_up = (0, -1)
dir_down = (0, 1)

def next_pos(xy, dir):
    x, y = xy
    dx, dy = dir
    return (x + dx, y + dy)

def new_dir(dir, mirror):
    if dir == dir_up:
        return {'/':dir_right, '\\':dir_left}[mirror]
    elif dir == dir_down:
        return {'/':dir_left, '\\':dir_right}[mirror]
    elif dir == dir_left:
        return {'/':dir_down, '\\':dir_up}[mirror]
    elif dir == dir_right:
        return {'/':dir_up, '\\':dir_down}[mirror]
    else:
        pass

def fun_house(lines: List[str]) -> List[str]:
    w, h = len(lines[0]), len(lines)
    grid = [list(line) for line in lines]
    start = next(((x, y) for x in range(w) for y in range(h) if grid[y][x] == '*'))
    x, y = start
    if x == 0:
        dir = dir_right
    elif x == w - 1:
        dir = dir_left
    elif y == 0:
        dir = dir_down
    else:
        dir = dir_up
    while grid[y][x] != 'x':
        x, y = next_pos((x, y), dir)
        if grid[y][x] in ['/', '\\']:
            dir = new_dir(dir, grid[y][x])
    grid[y][x] = '&'
    return [''.join(c for c in line_list) for line_list in grid]

def test_1():
    house_in = """
xxxxxxxxxxx
x../..\...x
x..../....x
*../......x
x.........x
xxxxxxxxxxx
"""[1:-1].split('\n')

    house_out = """
xxxxxxxxxxx
x../..\...x
x..../....x
*../......x
x.........x
xxxxxx&xxxx
"""[1:-1].split('\n')

    assert fun_house(house_in) == house_out

if __name__ == '__main__':
    house_nr = 0
    while True:
        w, h = map(int, input().split())
        if (w, h) == (0, 0):
            break
        house_nr += 1
        room = []
        for row in range(h):
            room.append(input())
        res = fun_house(room)
        print(f'HOUSE {house_nr}')
        print('\n'.join(res))
