from typing import Tuple, Sequence

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False    
    
        
    def __repr__(self):
        return f"Point({self.x},{self.y})"

def simulation(room_dimensions: Tuple[int, int],
               movements: Sequence[Tuple[str, int]]) -> Tuple[Point, Point]:
    location = Point(0, 0)
    tl = location
    for move in movements:
        if move[0] == 'r':
            v = Point(move[1], 0)
        elif move[0] == 'l':
            v = Point(-move[1], 0)
        elif move[0] == 'u':
            v = Point(0, move[1])
        elif move[0] == 'd':
            v = Point(0, -move[1])
        location += v
        tl += v
        tl.x = min(max(tl.x, 0), room_dimensions[0] - 1) 
        tl.y = min(max(tl.y, 0), room_dimensions[1] - 1) 
    return location, tl

assert simulation((4, 5),
    [('u', 3), ('r', 4)]) == (Point(4, 3), Point(3, 3))

while True:
    width, length = map(int, input().split())
    if not any([width, length]):
        break
    num_moves = int(input())
    moves = []
    for _ in range(num_moves):
        dir, dist = input().split()
        moves.append((dir, int(dist)))
    result = simulation((width, length), moves)
    print(f"Robot thinks {result[0].x} {result[0].y}")
    print(f"Actually at {result[1].x} {result[1].y}")
    
    