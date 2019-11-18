# https://open.kattis.com/problems/leftbeehind

def leftbeehind(sweet, sour):
    if sweet + sour == 13:
        return 'Never speak again.'
    elif sweet == sour:
        return 'Undecided.'
    elif sweet > sour:
        return 'To the convention.'
    else:
        return 'Left beehind.'


def test_leftbeehind():
    assert leftbeehind(17, 3) == 'To the convention.'


def test_2():
    assert leftbeehind(13, 14) == 'Left beehind.'


def test_3():
    assert leftbeehind(8, 5) == 'Never speak again.'


def test_4():
    assert leftbeehind(44, 44) == 'Undecided.'


if __name__ == '__main__':
    sweet, sour = list(map(int, input().split()))
    while sweet != 0 or sour != 0:
        print(leftbeehind(sweet, sour))
        sweet, sour = list(map(int, input().split()))
