
# https://open.kattis.com/problems/rijeci

def calc(turn):
    if turn == 0:
        return (1,0)
    else:
        a,b = calc(turn-1)
        return (b, a+b)

def rijeci(param):
    ab_count = calc(param)
    return f"{ab_count[0]} {ab_count[1]}"


def test_rijeci():
    assert rijeci(10) == '34 55'


if __name__ == '__main__':
    print(rijeci(int(input())))

