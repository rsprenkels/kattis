import sys
import math

# Save the Planet.
# Use less Fossil Fuel.

n = int(input())  # the number of points used to draw the surface of Mars.
land = []
tl,tr, ground = 0,0,0
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land.append(tuple([int(j) for j in input().split()]))
    for ndx, left in enumerate(land[:-1]):
        right = land[ndx+1]
        if left[1] == right[1] and (width := right[0] - left[0]) >= 1000:
            if width > tr - tl:
                tr, tl = right[0], left[0]
                ground = right[1]
                print(f"tl:{tl} tr:{tr} ground:{ground}", file=sys.stderr, flush=True)

x, y, hs, vs, f, r, p = 0,0,0,0,0,0,0
rotate, power = 0,0
hold_angle = 21

def above_ground() -> bool:
    return x >= tl and x <= tr

def sign(value) -> int:
    return 1 if value > 0 else -1

# game loop
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]
    target_dir = 0
    choice = ''

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if not above_ground():
        target_dir = 1 if x < tl else -1
        if sign(hs) != target_dir or abs(hs) >= 45:
            rotate,power = hold_angle * sign(hs), 4
            choice='ag 1'
        elif abs(hs) < 40:
            choice='ag 2'
            rotate,power = -hold_angle * target_dir, 4
        else:
            if y < 2900:
                choice='ag 3'
                rotate,power = 0 , 4
            else:
                choice='ag 4'
                rotate,power = 0 , 2

    else:
        if abs(hs) > 18:
            rotate = min(90,abs(hs)) * sign(hs)
            power =4
            choice='E 1'
        else:
            rotate = 2 * hs
            power = 4 if vs < -35 else 2
            choice='E 2'
        if y - ground < 50:
            rotate=0
            choice+='low'

    print(f"choice:{choice} s1:{sign(hs)} target_dir:{target_dir} hs:{hs} tr:{tr} ground:{ground}", file=sys.stderr, flush=True)

    # R P. R is the desired rotation angle. P is the desired thrust power.
    print(rotate, power)
