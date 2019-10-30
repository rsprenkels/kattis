# https://open.kattis.com/contests/wcvho8/problems/exactlyelectrical

import math

a, b = map(int, input().split())
c, d = map(int, input().split())

charge = int(input())

dist = abs(c - a) + abs(d - b)

if dist <= charge and (charge - dist) % 2 == 0:
    print('y')
else:
    print('n')
