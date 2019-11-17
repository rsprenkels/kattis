# https://open.kattis.com/problems/boatparts

def boatparts(total_parts, partlist):
    replaced = set()
    for day, part in enumerate(partlist):
        replaced.add(part)
        if len(replaced) == total_parts:
            return str(day + 1)
    return 'paradox avoided'


def test_1():
    assert boatparts(3, [
        'left_oar',
        'right_oar',
        'left_oar',
        'hull',
        'right_oar',
    ]) == '4'


def test_2():
    assert boatparts(4, [
        'motor',
        'hull',
        'left_oar',
        'hull',
        'motor',
    ]) == 'paradox avoided'


if __name__ == '__main__':
    total_parts, days = list(map(int, input().split()))
    partlist = []
    for _ in range(days):
        partlist.append(input())
    print(boatparts(total_parts, partlist))
