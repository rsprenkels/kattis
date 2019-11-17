# https://open.kattis.com/problems/thisaintyourgrandpascheckerboard

def iscorrect(board):
    board_size = len(board)
    for row in board:
        if len([square for square in row if square == 'W']) != board_size // 2:
            return False
        if 'WWW' in row or 'BBB' in row:
            return False
    for col in range(board_size):
        board_col = ''.join([board[row][col] for row in range(board_size)])
        if len([square for square in board_col if square == 'W']) != board_size // 2:
            return False
        if 'WWW' in board_col or 'BBB' in board_col:
            return False
    return True


def test_1():
    board = ['WBBW',
             'WBWB',
             'BWWB',
             'BWBW', ]
    assert iscorrect(board) == True


def test_2():
    board = ['BWBWWB',
             'WBWBWB',
             'WBBWBW',
             'BBWBWW',
             'BWWBBW',
             'WWBWBB', ]
    assert iscorrect(board) == False


if __name__ == '__main__':
    rows = []
    for _ in range(int(input())):
        rows.append(input())
    print(1 if iscorrect(rows) else 0)
