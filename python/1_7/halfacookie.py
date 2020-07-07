from typing import Tuple
import sys, math

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
    
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __repr__(self):
        return f"{self.x} {self.y}"


def cookie_parts(radius: float, x: float, y: float) -> Tuple[bool, Tuple[float, float]]:
    d = Point(x,y).length()
    if d > radius:
        return (False, (0.0, 0.0))
    A = radius * (radius * math.acos(d / radius) - d * math.sqrt(1.0 - d * d / (radius * radius)))
    rest = math.pi * radius * radius - A
    return (True, (rest, A))

assert cookie_parts(radius=5.5, x=5.0, y=5.0) == (False, (0.0, 0.0))

# print(cookie_parts(radius=10.0, x=5.0, y=0.0))

# assert cookie_parts(radius=10.0, x=5.0, y=0.0) == (True, (252.740780, 61.418485))

for line in sys.stdin:
    result = cookie_parts(*map(float, line.split()))
    if result[0]:
        print(f"{result[1][0]} {result[1][1]}")
    else:
        print('miss')

# from 365.5 rank 1045 to  367.2 rank 1039