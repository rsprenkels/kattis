import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


boost_used = False
turn = 0

def rotate(origin, point, angle_deg):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in degrees.
    """
    ox, oy = origin
    px, py = point
    angle = math.radians(angle_deg)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(qx), int(qy)

# game loop
while True:
    turn += 1
    # ncp_x: x position of the next check point
    # ncp_y: y position of the next check point
    # ncp_dist: distance to the next checkpoint
    # ncp_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, ncp_x, ncp_y, ncp_dist, ncp_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    thrust = 100

    if abs(ncp_angle) >= 90:
        thrust=0
    elif abs(ncp_angle) >= 40:
        thrust = 90 - abs(ncp_angle)
    elif not boost_used and ncp_dist > 5000 and abs(ncp_angle) < 10:
        boost_used = True
        thrust = 'BOOST'
    nx, ny = ncp_x, ncp_y
    if abs(ncp_angle) < 30:
        nx, ny = rotate((x,y), (ncp_x, ncp_y), ncp_angle)

    # Write an action using print
    print(f"nx:{nx} ny:{ny} ncp_angle:{ncp_angle} abs:{abs(ncp_angle)} thrust:{thrust}", file=sys.stderr, flush=True)

    # if turn >= 63: thrust = 0

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(f'{nx} {ny} {thrust}')
