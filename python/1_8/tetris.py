from typing import Sequence, Tuple

piece_1 = [
    [1],
    [1],
    [1],
    [1],
]

piece_2 = [
    [1,1],
    [1,1],
]

piece_3 = [
    [0,1,1],
    [1,1,0],
]

piece_4 = [
    [1,1,0],
    [0,1,1],
]

piece_5 = [
    [0,1,0],
    [1,1,1],
]

piece_6 = [
    [0,0,1],
    [1,1,1],
]

piece_7 = [
    [1,0,0],
    [1,1,1],
]


class Board():
    def __init__(self, columns: Sequence[int]):
        self.columns = columns

    def piece_options(self, piece: Sequence[Tuple]) -> int:
        options = 0
        for rotation in range(4):
            
            for start_col in range(len(self.columns)):
                    

def test_1():
    b = Board([2,1,1,1,0,1])
    assert b.piece_options(piece_5) == 5


