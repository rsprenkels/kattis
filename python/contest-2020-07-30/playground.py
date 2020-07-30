from copy import deepcopy


def gen(n):
    for a in range(1, 5):
        for b in range(1, 5):
            yield [a, b]


def gen_rec(n, sofar = None):
    if sofar == None:
        sofar = []
    if n > 1:
        for x in range(1, 5):
            yield from gen_rec(n - 1, sofar + [x])
    else:
        for x in range(1, 5):
            yield sofar + [x]

def g2(n, sofar = None):
    if sofar == None:
        sofar = {}
    if n > 1:
        for x in range(1, 5):
            yield from g2(n - 1, {**sofar,  **{len(sofar) + 1 : x}})
    else:
        for x in range(1, 5):
            yield {**sofar,  **{len(sofar) + 1 : x}}

def test_1():
    assert list(gen(2)) == [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]

def test_2():
    assert list(gen_rec(2)) == [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]

def test_g2():
    assert list(g2(2)) == [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]

def test_3():
    assert next(gen_rec(2)) == [1, 1]


