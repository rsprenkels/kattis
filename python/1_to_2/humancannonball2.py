import math

num_testcases = int(input())

for testcase in range(num_testcases):
    v0, phi, x1, h1, h2 = map(float, input().split())
    phi = math.radians(phi)
    # print(f"got {v0}, {phi}, {x1}, {h1}, {h2}")
    travel_time = x1 / (v0 * math.cos(phi))
    passing_altitude = v0 * travel_time * math.sin(phi) - 9.81 * travel_time * travel_time / 2.0
    # print(f"travel_time:{travel_time}  passing_altitude:{passing_altitude}")
    if passing_altitude > h1 + 1.0 and passing_altitude < h2 - 1.0:
        print('Safe')
    else:
        print('Not Safe')