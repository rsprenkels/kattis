def solution(h: int, k: int, v: int, s: int) -> int:
    x = 0
    while h > 0:
        v += s
        v -= max(1, int(v / 10.0))
        if v >= k:
            h += 1
        elif 0 < v and v < k:
            h -= 1
            if h == 0:
                v = 0
        else:
            h, v = (0, 0)
        x += v
        if s > 0:
            s -= 1
    return x

def test_1():
    assert solution(*[1, 1, 1, 1]) == 1
    assert solution(*[2, 2, 2, 2]) == 9
    assert solution(*[1, 2, 3, 4]) == 68
    assert solution(*[314, 159, 265, 358]) == 581062

if __name__ == '__main__':
    print(solution(*list(map(int, input().split(' ')))))