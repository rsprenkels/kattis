# https://open.kattis.com/problems/prozor

class Prozor():
    def __init__(self, picture, racket_size):
        self.picture = picture
        self.racket_size = racket_size

    def output(self):
        grid = self.picture
        max_killed_flies = 0
        best_spot = (0, 0)
        for y in range(len(grid) - (self.racket_size - 2)):
            for x in range(len(grid[y]) - (self.racket_size - 2)):
                killed_flies = 0
                for kill_y in range(y+1, y+1 + self.racket_size - 2):
                    killed_flies += len([p for p in grid[kill_y][x+1 : x+1 + self.racket_size - 2] if p == '*'])
                if killed_flies > max_killed_flies:
                    max_killed_flies = killed_flies
                    best_spot = (x, y)
        matrix = []
        for row in self.picture:
            matrix.append(list(row))

        best_x, best_y = best_spot
        for x in range(best_x + 1, best_x + self.racket_size  -1):
            matrix[best_y][x] = '-'
            matrix[best_y + self.racket_size - 1][x] = '-'
        for y in range(best_y+1, best_y + self.racket_size - 1):
            matrix[y][best_x] = '|'
            matrix[y][best_x + self.racket_size - 1] = '|'
        matrix[best_y][best_x] = '+'
        matrix[best_y][best_x + self.racket_size - 1] = '+'
        matrix[best_y + self.racket_size - 1][best_x] = '+'
        matrix[best_y + self.racket_size - 1][best_x + self.racket_size - 1] = '+'

        return (max_killed_flies, [''.join(row) for row in matrix])

def test_1():
    picture = \
        [
            '.....',
            '.*.*.',
            '.....',
        ]
    assert Prozor(picture, racket_size=3).output() == (1,
        [
            '+-+..',
            '|*|*.',
            '+-+..',
        ])

def test_2():
    picture = \
        [
            '......',
            '.*.*.*',
            '......',
            '.*.*..',
            '..*...',
            '..*...',
            '*....*',
        ]
    assert Prozor(picture, racket_size=4).output() == (2,
                                                       [
                                                       '......',
                                                       '.*.*.*',
                                                       '+--+..',
                                                       '|*.|..',
                                                       '|.*|..',
                                                       '+--+..',
                                                       '*....*',
                                                       ])



def test_3():
    picture = \
        [
            '***......',
            '......*.*',
            '.*....*..',
            '..*...*..',
            '..*.*....',
            '..*....*.',
            '.....*...',
            '.*...***.',
            '.........',
        ]
    assert Prozor(picture, racket_size=6).output() == (6,
                                                       [
                                                       '***......',
                                                       '......*.*',
                                                       '.*....*..',
                                                       '..*+----+',
                                                       '..*|*...|',
                                                       '..*|...*|',
                                                       '...|.*..|',
                                                       '.*.|.***|',
                                                       '...+----+',
                                                       ])


if __name__ == '__main__':
    rows, cols, racket_size = list(map(int, input().split()))
    picture = []
    for _ in range(rows):
        picture.append(input())
    result = Prozor(picture, racket_size).output()
    print(result[0])
    for line in result[1]:
        print(line)
