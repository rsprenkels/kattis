import sys
from typing import Sequence

class Board():
    def __init__(self, ascii_form : Sequence[str]):
        self.pieces = []
        for row in range(8):
            for col in range (8):
                piece_type = ascii_form[row * 2 + 1][col * 4 + 2]
                if piece_type not in '.:':
                    self.pieces.append(Piece(is_white=piece_type.isupper(), piece_type=piece_type, row=7 - row, col=col))

    def __repr__(self):
        lines = []
        lines.append(f'White: {",".join(map(str, sorted([p for p in self.pieces if p.is_white])))}')
        lines.append(f'Black: {",".join(map(str, sorted([p for p in self.pieces if p.is_black])))}')
        return '\n'.join(lines)

class Piece():
    def __init__(self, is_white: bool, piece_type: str, col: int, row: int):
        self.is_white = is_white
        self.is_black = not is_white
        self.piece_type = 'PNBRQK'.find(piece_type.upper())
        self.col, self.row = col, row

    def __lt__(self, other):
        if self.piece_type != other.piece_type:
            return self.piece_type > other.piece_type
        elif self.row != other.row:
            if self.is_white:
                return self.row < other.row
            else:
                return self.row > other.row
        else:
            return self.col < other.col

    def __repr__(self):
        return f'{["", "N", "B", "R", "Q", "K"][self.piece_type]}{"abcdefgh"[self.col]}{self.row + 1}'

def test_boardreader_1():
    board = """
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
"""[1:-1].split()
    b = Board(board)
    assert f'{b}' == """
White: Ke1,Qd1,Ra1,Rh1,Bc1,Bf1,Nb1,a2,c2,d2,f2,g2,h2,a3,e4
Black: Ke8,Qd8,Ra8,Rh8,Bc8,Ng8,Nc6,a7,b7,c7,d7,e7,f7,h7,h6
"""[1:-1]

def test_boardreader_2():
    board = """
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
"""[1:-1].split()
    b = Board(board)
    print(b)

    assert f'{b}' == """
White: 
Black: Kh5,Ke1
"""[1:-1]

if __name__ == '__main__':
    board = sys.stdin.readlines()
    b = Board(board)
    print(b)

# from 419.0 rank 875 to 421.4 rank 872
