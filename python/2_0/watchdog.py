import math
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

    def mhdist(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def dist(self, other) -> float:
        return math.sqrt(math.pow(abs(self.x - other.x), 2) + math.pow(abs(self.y - other.y), 2))

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __repr__(self):
        return f"{self.x} {self.y}"


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs


def watchdog(roof_size: int, hatches : Sequence[Point]) -> Tuple[bool, Point]:
    for x in range(1, roof_size):
        for y in range(1, roof_size):
            candidate = Point(x, y)
            if candidate not in hatches:
                longest_leash = max([candidate.dist(h) for h in hatches])
                if candidate.x >= longest_leash and candidate.x <= roof_size - longest_leash and candidate.y >= longest_leash and candidate.y <= roof_size - longest_leash:
                    return (True, candidate)
    return (False, Point(0,0))
    
assert watchdog(10, [Point(6,6), Point(5,4)]) == (True, Point(3, 6))

assert watchdog(20, [Point(1,1), Point(19,19)]) == (False, Point(0, 0))

for _ in range(int(input())):
    roof_size, num_hathes = map(int, input().split())
    hatches = []
    for _ in range(num_hathes):
        hatches.append(Point(*map(int, input().split())))
    result = watchdog(roof_size, hatches)
    if result[0]:
        print(result[1])
    else:
        print('poodle')

# from 370.9 rank 1025 to 372.9 rank 1019