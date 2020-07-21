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

class Target():
    def __init__(self):
        raise Exception('Target is abstract class, do not instantiate')

    def overlaps(self, x:int, y:int) -> bool:
        raise Exception('Target.overlap() must be overridden')

class Rectangle(Target):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def overlaps(self, x:int, y:int) -> bool:
        return x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2

class Circle(Target):
    def __init__(self, x: int, y: int, radius : int):
        self.centre = Point(x, y)
        self.radius = radius

    def overlaps(self, x:int, y:int) -> bool:
        return (self.centre - Point(x,y)).length() <= self.radius

class TargetSet():
    def __init__(self):
        self.targets = []

    def targetsAt(self, x: int, y: int) -> int:
        return len([t for t in self.targets if t.overlaps(x, y)])

def test_basic():
    try:
        t = Target()
    except:
        assert True
    else:
        assert False

def test_ht_circle():
    targets = []
    targets.append(Circle(x=5, y=0, radius=8))
    assert targets[0].overlaps(x=4, y=4) == True
    assert targets[0].overlaps(x=100, y=100) == False

def test_ht_rectangle():
    targets = []
    targets.append(Rectangle(1, 1, 10, 5))
    assert targets[0].overlaps(x=4, y=4) == True
    assert targets[0].overlaps(x=100, y=100) == False

def test_targetset():
    ts = TargetSet()
    ts.targets.append(Circle(5, 0, 8))
    ts.targets.append(Rectangle(2, 2, 9, 9))
    assert ts.targetsAt(1, 1) == 1
    assert ts.targetsAt(3, 3) == 2
    assert ts.targetsAt(100,200) == 0

if __name__ == '__main__':
    ts = TargetSet()
    for _ in range(int(input())):
        target = input().split()
        if target[0] == 'rectangle':
            x1, y1, x2, y2 = list(map(int, target[1:]))
            ts.targets.append(Rectangle(x1, y1, x2, y2))
        else:
            x, y, radius = list(map(int, target[1:]))
            ts.targets.append(Circle(x, y, radius))
    for _ in range(int(input())):
        print(ts.targetsAt(*list(map(int, input().split()))))

# from 417.3 rank 879 to 419.0 rank 875
