# https://open.kattis.com/problems/unlockpattern
from math import sqrt


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def path_len(boardlist):
    board = {}
    for y, row in enumerate(boardlist):
        for x, number in enumerate(row.split()):
            board[int(number)] = (x, y)
    distance_covered = 0.0
    for position in range(2, 10):
        distance_covered += dist(board[position - 1], board[position])
    return distance_covered


def test_unlockpattern():
    sample_input = [
        '6 1 9',
        '5 2 8',
        '4 3 7', ]
    assert path_len(sample_input) - 9.8284271247 <= 0.0000001


if __name__ == '__main__':
    boardlist = []
    for _ in range(3):
        boardlist.append(input())
    print(path_len(boardlist))
