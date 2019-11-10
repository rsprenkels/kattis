def hothike(temps):
    best = sorted([(i, max(temps[i], temps[i+2])) for i in range(len(temps) - 2)], key = lambda x : x[1])[0]
    return [best[0] + 1, best[1]]

def test_hothike():
    assert hothike(list(map(int, "23 27 31 28 30".split()))) == [2, 28]

if __name__ == '__main__':
    input()
    result = hothike(list(map(int, input().split())))
    print(f"{result[0]} {result[1]}")