# https://open.kattis.com/problems/flyingsafely
from collections import defaultdict


def shortest_spanning_tree(cities, start_node, tree, seen):
    to_visit = [n for n in tree[start_node] if n not in seen]
    print(to_visit)


def flyingsafely(cities, schedule):
    connected = defaultdict(set)
    for flight in schedule:
        a, b = flight
        connected[a].add(b)
        connected[b].add(a)
    return shortest_spanning_tree(cities=cities, start_node=list(connected.keys())[0],
                                  tree=connected, seen=set())


def test_1():
    assert flyingsafely(cities=3, schedule=[(1, 2), (2, 3), (1, 3), ]) == 2


def test_2():
    assert flyingsafely(cities=5, schedule=[(2, 1), (2, 3), (4, 3), (4, 5), ]) == 4
