from typing import Sequence


def put_on_board(board: Sequence[str], piece: str, case_function):
    if len(piece) == 3:
        piece_letter = piece[0]
        piece = piece[1:]
    else:
        piece_letter = 'P'
    row, col = 8 - int(piece[1]), 'abcdefgh'.index(piece[0])
    board[row*2 + 1][col*4+2] = case_function(piece_letter)

def board_to_ascii(lines: Sequence[str]) -> Sequence[str]:
    # to not break detecting if there are any pieces
    lines = [l.strip() for l in lines]
    board_lines = ['' for _ in range(17)]
    for row in range(0, 17, 2):
        board_lines[row] = '+---+---+---+---+---+---+---+---+'
    for row in range(1, 17, 4):
        board_lines[row] = '|...|:::|...|:::|...|:::|...|:::|'
    for row in range(3, 17, 4):
        board_lines[row] = '|:::|...|:::|...|:::|...|:::|...|'
    board = [[c for c in line] for line in board_lines]
    white_pieces = lines[0].split(' ')
    if len(white_pieces) == 2:
        # there are actually white pieces
        for piece in white_pieces[1].split(','):
            put_on_board(board, piece, str.upper)
    black_pieces = lines[1].split(' ')
    if len(black_pieces) == 2:
        # there are actually black pieces
        for piece in black_pieces[1].split(','):
            put_on_board(board, piece, str.lower)
    return [''.join([b for b in bl]) for bl in board]

def test_1():

    board = [
        'White: Ke1,Qd1,Ra1,Rh1,Bc1,Bf1,Nb1,a2,c2,d2,f2,g2,h2,a3,e4',
        'Black: Ke8,Qd8,Ra8,Rh8,Bc8,Ng8,Nc6,a7,b7,c7,d7,e7,f7,h7,h6',
    ]

    t = """
+---+---+---+---+---+---+---+---+
|.r.|:::|.b.|:q:|.k.|:::|.n.|:r:|
+---+---+---+---+---+---+---+---+
|:p:|.p.|:p:|.p.|:p:|.p.|:::|.p.|
+---+---+---+---+---+---+---+---+
|...|:::|.n.|:::|...|:::|...|:p:|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|.P.|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:P:|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|.P.|:::|.P.|:P:|...|:P:|.P.|:P:|
+---+---+---+---+---+---+---+---+
|:R:|.N.|:B:|.Q.|:K:|.B.|:::|.R.|
+---+---+---+---+---+---+---+---+
"""[1:-1]
    assert '\n'.join(board_to_ascii(board)) == t

def test_2():
    board = [
        'White: ',
        'Black: Kh5,Ke1'
    ]

    t = """
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|.k.|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:k:|...|:::|...|
+---+---+---+---+---+---+---+---+
"""[1:-1]
    assert '\n'.join(board_to_ascii(board)) == t


if __name__ == '__main__':
    board = [input(), input()]
    print('\n'.join(board_to_ascii(board)))

# from 428.3 rank 853 to 430.0 rank 849