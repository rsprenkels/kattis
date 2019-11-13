# https://open.kattis.com/problems/cudoviste

def count_symbols(symbol, x, y, city_map) -> int:
    row_1 =  sum([1 for index in [x, x+1] if city_map[y][index] == symbol])
    row_2 =  sum([1 for index in [x, x+1] if city_map[y+1][index] == symbol])
    return row_1 + row_2


def cudoviste(city_map):
    squash_cars = [0] * 5
    for y in range(len(city_map) - 1):
        for x in range(len(city_map[0]) - 1):
            if count_symbols('#', x, y, city_map) >= 1:
                continue
            squash_cars[count_symbols('X', x, y, city_map)] += 1
    return squash_cars


city_map = ['#..#',
            '..X.',
            '..X.',
            '#XX#']

map_2 = ['..XX.',
         '.#XX.',
         '..#..',
         '.....',
         ]

def test_cudoviste():
    assert cudoviste(city_map) == [1,1,2,1,0]

def test_map2():
    assert cudoviste(map_2) == [2,1,1,0,1]

def test_counter():
    assert count_symbols('#', 0, 0, city_map) == 1
    assert count_symbols('#', 1, 0, city_map) == 0
    assert count_symbols('#', 2, 0, city_map) == 1
    assert count_symbols('#', 0, 0, city_map) == 1
    assert count_symbols('#', 0, 0, city_map) == 1

def test_c2():
    assert count_symbols('X', 2, 1, city_map) == 2


if __name__ == '__main__':
    R, C = list(map(int, input().split()))
    the_map = []
    for _ in range(R):
        the_map.append(input())
    for num_smash in cudoviste(the_map):
        print(num_smash)