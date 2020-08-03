from typing import Sequence, Tuple, Set


def on_board(k: Tuple[int, int]) -> bool:
    return k[0] >= 0 and k[0] < 5 and k[1] >= 0 and k[1] < 5

def tup_add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])

def attacks(k: Tuple[int, int]) -> Set[Tuple[int, int]]:
    return {tup_add(k, offset) for offset in {(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)} if on_board(tup_add(k, offset))}

def isvalid(board: Sequence[str]) -> bool:
    knights = {(row, col) for col in range(5) for row in range(5) if board[row][col] == 'k'}
    if len(knights) != 9:
        return False
    for k in knights:
        if attacks(k).intersection(knights):
            return False
    return True

def test_1():
    board = """
...k.
...k.
k.k..
.k.k.
k.k.k
"""[1:-1].split('\n')
    assert isvalid(board) == False


def test_2():
    board = """
.....
...k.
k.k.k
.k.k.
k.k.k
"""[1:-1].split('\n')
    assert isvalid(board) == True


def test_3():
    board = """
.....
...k.
k.k.k
.k.k.
k...k
"""[1:-1].split('\n')
    assert isvalid(board) == False

if __name__ == '__main__':
    board = []
    for _ in range(5):
        board.append(input())
    if isvalid(board):
        print('valid')
    else:
        print('invalid')

# nice one, a solution with 8 knights is still NOT valid.....
# from 459.1 rank 789 to
