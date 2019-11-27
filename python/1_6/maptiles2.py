# https://open.kattis.com/problems/maptiles2

def maptiles2(quadkey):
    zoomlevel = len(quadkey)
    x, y = (0, 0)
    for step in [int(qk) for qk in quadkey]:
        sx, sy = (step % 2, step // 2)
        x = 2 * x + sx
        y = 2 * y + sy
    return (zoomlevel, x, y)


def test_1():
    assert maptiles2('3') == (1, 1, 1)


def test_2():
    assert maptiles2('130') == (3, 6, 2)


if __name__ == '__main__':
    print(' '.join([str(c) for c in list(maptiles2(input()))]))
