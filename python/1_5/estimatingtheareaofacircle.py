import math

def estimate(radius, marked_points, in_circle):
    return math.pi * radius * radius, 4 * in_circle / marked_points * radius * radius

# assert estimate(radius=1.0, marked_points=100, in_circle=75) == (3.141592654, 3)

while True:
    radius, marked_points, in_circle = list(map(float, input().split()))
    if (radius, marked_points, in_circle) != (0.0, 0.0, 0.0):
        result = (estimate(radius, marked_points, in_circle))
        print(f"{result[0]} {result[1]}")
    else:
        break
                                            