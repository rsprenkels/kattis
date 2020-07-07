import math

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
