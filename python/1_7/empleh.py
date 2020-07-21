from typing import Sequence


def board_to_ascii(lines: Sequence[str]) -> Sequence[str]:
    board = ['' for _ in range(17)]
    for row in range(0, 17, 2):
        board[row] = '+---+---+---+---+---+---+---+---+'
    for row in range(1, 17, 4):
        board[row] = '|...|:::|...|:::|...|:::|...|:::|'
    for row in range(3, 17, 4):
        board[row] = '|:::|...|:::|...|:::|...|:::|...|'
    white_pieces = lines[0].split(' ')
    if len(white_pieces) == 2:
        # there are actually white pieces
        for piece in white_pieces[1].split(','):

    black_pieces = lines[1].split(' ')
    if len(black_pieces) == 2:
        # there are actually black pieces
        pass
    return board

print('\n'.join(board_to_ascii(['',''])))

