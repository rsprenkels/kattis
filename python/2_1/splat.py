# https://open.kattis.com/problems/splat
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

class Drop():
    def __init__(self, x:float, y:float, v:float, color: str):
        self.location = Point(x, y)
        self.radius = math.sqrt((v / math.pi))
        self.color = color

    def in_range(self, p: Point) -> bool:
        return (self.location - p).length() <= self.radius

class Painting():
    def __init__(self):
        self.drops = []
        self.queries = []

    def add_drop(self, x, y, v, color):
        self.drops.append(Drop(x, y, v, color))

    def add_query(self, x: int, y: int):
        self.queries.append(Point(x, y))

    def get_query_results(self):
        drops_hit =  [(['white'] + [d.color for d in self.drops if d.in_range(q)])[-1] for q in self.queries]
        return drops_hit

def test():
    p = Painting()
    p.add_drop(x=0, y=0, v=4, color='blue')
    p.add_drop(x=2, y=3, v=8, color='red')
    p.add_drop(x=4, y=3, v=10, color='green')
    p.add_query(1.1, 0)
    p.add_query(2, 3)
    p.add_query(6, 6)
    print(p.get_query_results())
    assert p.get_query_results() == ['blue', 'red', 'white']

if __name__ == '__main__':
    num_paintings = int(input())
    for _ in range(num_paintings):
        p = Painting()
        for _ in range(int(input())):
            x, y, v, color = input().split()
            p.add_drop(float(x), float(y), float(v), color)
        for _ in range(int(input())):
            p.add_query(*list(map(float, input().split())))
        print('\n'.join(p.get_query_results()))

# from 383,4 rank 978 to 385.5 rank 971
