from typing import Tuple, Sequence

def cake_length(width: int, pieces: Sequence[Tuple[int, int]]) -> int:
    total_area = sum([p[0]*p[1] for p in pieces])
    return total_area // width


assert cake_length(width=4,
    pieces=[(2,3),(1,4),(1,2),(1,2),(2,2),(2,2),(2,1)]) == 6

width = int(input())
num_pieces = int(input())
pieces = []
for _ in range(num_pieces):
    pieces.append(tuple(map(int, input().split())))
print(cake_length(width, pieces))

# from 360.9 rank 1060 to 362.5 1056