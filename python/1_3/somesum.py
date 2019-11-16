# https://open.kattis.com/problems/somesum

def somesum(N):
    res_odd = sum(range(1, N + 1))
    res_even = sum(range(2, N + 2))
    if res_odd % 2 == 0 and res_even % 2 == 0:
        return 'Even'
    elif res_odd % 2 == 1 and res_even % 2 == 1:
        return 'Odd'
    else:
        return 'Either'


def test_1():
    assert somesum(1) == 'Either'


def test_2():
    assert somesum(2) == 'Odd'


def test_4():
    assert somesum(4) == 'Even'


if __name__ == '__main__':
    print(somesum(int(input())))
