from collections import defaultdict
from typing import Sequence, Tuple, Set, DefaultDict, Dict


def dijkstra(num_nodes: int, edges: Sequence[Tuple[int, int, int]], start_node: int, queries: Sequence[int]) -> Sequence[Tuple[bool, int]]:
    tree: DefaultDict[Set[Tuple[int, int]]] = defaultdict(set)
    Q: Set[int] = set()
    dist: Sequence[int] = [999999999999999] * num_nodes
    for edge in edges:
        a, b, cost = edge
        tree[a].add((b, cost))
    for n in range(num_nodes):
        Q.add(n)
    dist[start_node] = 0

    while Q:
        v = min([(dist[v], v) for v in Q])[1]
        Q.remove(v)
        for u in [u for u in tree[v] if u[0] in Q]:
            alt = dist[v] + u[1]
            if alt < dist[u[0]]:
                dist[u[0]] = alt
    result = []
    for q in queries:
        if dist[q] < 999999999999999:
            result.append((True, dist[q]))
        else:
            result.append((False, 0))
    return result

def test_dijkstra():
    edges = [(0, 1, 2), (1, 2, 2), (3, 0, 2)]
    start_node = 0
    queries = [0, 1, 2, 3]
    assert dijkstra(4, edges, start_node, queries) == [(True, 0), (True, 2), (True, 4), (False, 0)]

def test_2():
    # look at https://networkx.github.io/documentation/stable/tutorial.html
    # background stuff: http://www.cs.uu.nl/docs/vakken/an/an-shortestpaths-2017.pdf
    pass

if __name__ == '__main__':
    while True:
        nmqs = list(map(int, input().split()))
        if all([x == 0 for x in nmqs]):
            break
        n, m, q, s = nmqs
        edges = []
        for _ in range(m):
            edges.append(tuple(map(int, input().split())))
        queries = []
        for _ in range(q):
            queries.append(int(input()))
        for r in dijkstra(n, edges, s, queries):
            possible, dist = r
            if possible:
                print(dist)
            else:
                print('Impossible')
        print()
