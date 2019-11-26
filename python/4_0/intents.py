# https://open.kattis.com/problems/intents
import math
from itertools import permutations


def triangle_area(p1, p2, p3):
    ax, ay = p1
    bx, by = p2
    cx, cy = p3
    return abs((ax * (by-cy) + bx * (cy-ay) + cx * (ay - by)) / 2)


def intents(num_poles, points, lengths):
    longest_pole = max(lengths)
    poles = [l for l in lengths if l != longest_pole]

    sorted_points = sorted(points, key=lambda p : math.atan2(p[1], p[0]))

    perm = permutations(poles)
    max_volume = 0.0
    for one_order in list(perm):
        volume = 0.0
        for index, length in enumerate(one_order):
            p1 = sorted_points[index]
            p2 = sorted_points[(index + 1) % (num_poles - 1)]
            p3 = (0,0)
            len_1 = length
            len_2 = one_order[(index + 1) % len(poles)]
            len_3 = longest_pole
            base_area = triangle_area(p1, p2, p3)
            volume += base_area * (len_1 + len_2 + len_3) / 3.0
        if volume > max_volume:
            max_volume = volume
    return max_volume


def intents_fast(num_poles, points, lengths) -> float:
    longest_pole = max(lengths)
    poles = [l for l in lengths if l != longest_pole]
    sorted_points = sorted(points, key=lambda p : math.atan2(p[1], p[0]))
    for first_pole in poles:
        second_poles = [p for p in poles if p != first_pole]
        for second_pole in second_poles:
            print(f"checking as pole combination {first_pole} {second_pole}")
            rest_poles = [p for p in second_poles if p != second_pole] # >= 1 rest_poles


def test_intents():
    num_poles = 5
    points = [(100, 100), (-200, -200), (300, -300), (-400, 400),]
    lengths = [30, 20, 50, 60, 10,]
    assert abs(intents(num_poles, points, lengths) - 8566666.666667) <= 0.001


def test_intents_fast():
    num_poles = 5
    points = [(100, 100), (-200, -200), (300, -300), (-400, 400),]
    lengths = [30, 20, 50, 60, 10,]
    assert abs(intents_fast(num_poles, points, lengths) - 8566666.666667) <= 0.001


if __name__ == '__main__':
    num_poles = int(input())
    locations = []
    for _ in range(num_poles - 1):
        locations.append(tuple(list(map(int, input().split()))))
    poles = []
    for _ in range(num_poles):
        poles.append(int(input()))
    print(intents(num_poles, locations, poles))