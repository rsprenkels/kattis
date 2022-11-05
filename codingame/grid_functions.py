from __future__ import annotations
import sys
import math
from dataclasses import dataclass, field
from functools import reduce

# The machines are gaining ground. Time to show them what we're really made of...
from typing import List, Type


@dataclass
class Node:
    x:int
    y:int
    links: int = 0
    left: Type['Node'] = None
    right: Type['Node'] = None
    up: Type['Node'] = None
    down: Type['Node'] = None
    link_count : List[int] = field(default_factory=lambda: [0,0,0,0])

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        res = f'({self.x}{self.y})'
        res += f'{self.left.x}{self.left.y}-' if self.left else '  -'
        res += f'{self.right.x}{self.right.y}-' if self.right else '  -'
        res += f'{self.up.x}{self.up.y}-' if self.up else '  -'
        res += f'{self.down.x}{self.down.y}-' if self.down else '  -'
        return res

def spanning_tree(nodes: List[Node]) -> bool:
    return True
    Q = []
    seen = []
    Q.append(nodes[0])
    while Q:
        n = Q.pop(0)
        seen.append(n)
        if n.link_count[0]>0 and n.left not in seen and n.left not in Q:
            Q.append(n.left)
        if n.link_count[1]>0 and n.right not in seen and n.right not in Q:
            Q.append(n.right)
        if n.link_count[2]>0 and n.up not in seen and n.up not in Q:
            Q.append(n.up)
        if n.link_count[3]>0 and n.down not in seen and n.down not in Q:
            Q.append(n.down)
    # print(f'{seen} ls:{len(seen)} ln:{len(nodes)}', file=sys.stderr, flush=True)
    return len(seen) == len(nodes)



def solveLinks(nodes : List[Node]) -> bool:
    if reduce(lambda a,b: a and b, [(sum(n.link_count) == n.links) for n in nodes]):
        if spanning_tree(nodes):
            return True
    for n in [n for n in nodes if sum(n.link_count) < n.links]:
        for direction in ['left','right','up','down']:
            if direction == 'left' and n.left and n.link_count[0] < 2 and sum(n.left.link_count) < n.left.links:
                n.link_count[0] += 1
                n.left.link_count[1] += 1
                if solveLinks(nodes):
                    return True
                n.link_count[0] -= 1
                n.left.link_count[1] -= 1
            if direction == 'right' and n.right and n.link_count[1] < 2 and sum(n.right.link_count) < n.right.links:
                n.link_count[1] += 1
                n.right.link_count[0] += 1
                if solveLinks(nodes):
                    return True
                n.link_count[1] -= 1
                n.right.link_count[0] -= 1
            if direction == 'up' and n.up and n.link_count[2] < 2 and sum(n.up.link_count) < n.up.links:
                n.link_count[2] += 1
                n.up.link_count[3] += 1
                if solveLinks(nodes):
                    return True
                n.link_count[2] -= 1
                n.up.link_count[3] -= 1
            if direction == 'down' and n.down and n.link_count[3] < 2 and sum(n.down.link_count) < n.down.links:
                n.link_count[3] += 1
                n.down.link_count[2] += 1
                if solveLinks(nodes):
                    return True
                n.link_count[3] -= 1
                n.down.link_count[2] -= 1
        return False

def maze(width: int, height:int, lines: List[str]) -> None:
    nodes = []

    # print(f'width:{width} height:{height}', file=sys.stderr, flush=True)
    for y in range(height):
        line = lines[y]  # width characters, each either a number or a '.'
        # print(line, file=sys.stderr, flush=True)
        for x, c in enumerate(line):
            if c != '.':
                #print(f'x:{x} y:{y} c:{c}', file=sys.stderr, flush=True)
                nodes.append(Node(x,y,int(c)))

    for n in nodes:
        if n.left == None:
            # print(f'left {n}', file=sys.stderr, flush=True)
            for x in range(n.x-1, -1, -1):
                if (other_node := Node(x, n.y)) in nodes:
                    on = [x for x in nodes if x == other_node][0]
                    n.left = on
                    on.right = n
                    break
        if n.right == None:
            # print(f'right {n}', file=sys.stderr, flush=True)
            for x in range(n.x+1, width):
                # print(f'checking {x} {Node(x, n.y)}', file=sys.stderr, flush=True)
                if (other_node := Node(x, n.y)) in nodes:
                    # print(f'D1 {other_node}', file=sys.stderr, flush=True)
                    on = [k for k in nodes if k == other_node][0]
                    n.right = on
                    on.left = n
                    break
        if n.up == None:
            for y in range(n.y-1, -1, -1):
                if (other_node := Node(n.x, y)) in nodes:
                    on = [k for k in nodes if k == other_node][0]
                    n.up = on
                    on.down = n
                    break
        if n.down == None:
            for y in range(n.y+1, height):
                if (other_node := Node(n.x, y)) in nodes:
                    on = [k for k in nodes if k == other_node][0]
                    n.down = on
                    on.up = n
                    break

    # for n in nodes:
    #     print(f'n:{n}', file=sys.stderr, flush=True)

    if (result := solveLinks(nodes)) or True:
        print(f'result:{result}', file=sys.stderr, flush=True)
        while (toprint := [n for n in nodes if sum(n.link_count) > 0]):
            n = toprint[0]
            if (num_links := n.link_count[0]) > 0:
                print(f'{n.x} {n.y} {n.left.x} {n.left.y} {num_links}')
                n.link_count[0] = 0
                n.left.link_count[1] = 0
                continue
            if (num_links := n.link_count[1]) > 0:
                print(f'{n.x} {n.y} {n.right.x} {n.right.y} {num_links}')
                n.link_count[1] = 0
                n.right.link_count[0] = 0
                continue
            if (num_links := n.link_count[2]) > 0:
                print(f'{n.x} {n.y} {n.up.x} {n.up.y} {num_links}')
                n.link_count[2] = 0
                n.up.link_count[3] = 0
                continue
            if (num_links := n.link_count[3]) > 0:
                print(f'{n.x} {n.y} {n.down.x} {n.down.y} {num_links}')
                n.link_count[3] = 0
                n.down.link_count[2] = 0
                continue
    else:
        print('NO solution found')

# width = int(input())
# height = int(input())
# lines = []
# for _ in range(height):
#     lines.append(input())

# print(f'{lines}', file=sys.stderr, flush=True)

# maze(width, height, lines)
# maze(3, 3, ['242','...','...'])

# maze(width, height, lines)
maze(5, 14, ['22221', '2....', '2....', '2....', '2....', '22321', '.....', '.....', '22321', '2....', '2....', '2.131', '2..2.', '2222.'])



#hoe werkt dit dan:
def is_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

f,*numbers = map(int,open(0))

print(max(filter(is_prime,numbers)))


