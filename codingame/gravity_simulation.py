# Simple pygame program
from dataclasses import dataclass
import pygame, math
from random import randrange, uniform
scr_width, scr_height = 1200,1000

# Import and initialize the pygame library
@dataclass
class Vector_old:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __abs__(self):
        """Absolute value (magnitude) of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

@dataclass
class Point:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

class Vector:
    """A two-dimensional vector with Cartesian coordinates."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """Human-readable string representation of the vector."""
        return '{:g}i + {:g}j'.format(self.x, self.y)

    def __repr__(self):
        """Unambiguous string representation of the vector."""
        return repr((self.x, self.y))

    def dot(self, other):
        """The scalar (dot) product of self and other. Both must be vectors."""

        if not isinstance(other, Vector):
            raise TypeError('Can only take dot product of two Vector objects')
        return self.x * other.x + self.y * other.y
    # Alias the __matmul__ method to dot so we can use a @ b as well as a.dot(b).
    __matmul__ = dot

    def __sub__(self, other):
        """Vector subtraction."""
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """Vector addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Multiplication of a vector by a scalar."""

        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x*scalar, self.y*scalar)
        raise NotImplementedError('Can only multiply Vector by a scalar')

    def __rmul__(self, scalar):
        """Reflected multiplication so vector * scalar also works."""
        return self.__mul__(scalar)

    def __neg__(self):
        """Negation of the vector (invert through origin.)"""
        return Vector(-self.x, -self.y)

    def __truediv__(self, scalar):
        """True division of the vector by a scalar."""
        return Vector(self.x / scalar, self.y / scalar)

    def __mod__(self, scalar):
        """One way to implement modulus operation: for each component."""
        return Vector(self.x % scalar, self.y % scalar)

    def __abs__(self):
        """Absolute value (magnitude) of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        """The distance between vectors self and other."""
        return abs(self - other)

    def to_polar(self):
        """Return the vector's components in polar coordinates."""
        return self.__abs__(), math.atan2(self.y, self.x)

@dataclass
class Object:
    id: int
    location: Point
    speed: Vector
    mass: float
    f : Vector = Vector(0,0)

    def draw(self):
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        text = font.render(f'{self.mass}', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (self.location.x, self.location.y)
        pygame.draw.circle(screen, color=(0, 0, 255), center=(self.location.x, self.location.y), radius=20)
        screen.blit(text, textRect)

    def __post_init__(self):
        self.speed = self.speed * 1
        self.mass = self.mass**2

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

objects = []

# for id in range(2):
#     objects.append(Object(id = id,location=Point(randrange(0,scr_width),randrange(0, scr_height)), speed=Vector(uniform(-10,10),uniform(-10,10)), mass=randrange(1,9)))

objects.append(Object(id = 1,location=Point(500,100), speed=Vector(120,0), mass=1))
objects.append(Object(id = 2,location=Point(500,500), speed=Vector(-0,0), mass=10))

# Set up the drawing window
screen = pygame.display.set_mode([scr_width, scr_height])

# Run until the user asks to quit
running = True

def chaos(dt : int):
    global ob
    dt = dt / 100
    # print(dt)
    # for ob in objects:
    #     ob.location.x += ob.speed.x * dt
    #     if ob.location.x < 0 or ob.location.x >= scr_width:
    #         ob.speed.x *= -1
    #     ob.location.y += ob.speed.y * dt
    #     if ob.location.y < 0 or ob.location.y >= scr_height:
    #         ob.speed.y *= -1
    for ob in objects:
        ob.speed += (ob.f / ob.mass) * dt
        ob.location += ob.speed * dt + (ob.f / ob.mass) * dt**2

def gravity(dt : int):
    # global ob
    # print('gravity')
    for ob in objects:
        ob.f = Vector(0,0)
        for ot_ob in [x for x in objects if x != ob]:
            ob.f += 100 * (ob.mass * ot_ob.mass) / (max(200, abs(ob.location - ot_ob.location)**2)) * (ot_ob.location - ob.location)
        # print(f'id:{ob.id} f:{ob.f}')
    chaos(dt)

simulate = gravity

clock = pygame.time.Clock()

while running:

    dt = clock.tick(60)

    simulate(dt)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for ob in objects:
        ob.draw()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()