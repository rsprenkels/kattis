# https://open.kattis.com/problems/heirsdilemma
import itertools


def heirsdilemma(L, H):
    safe_combis = 0
    for combi in itertools.permutations(list(range(1, 10)), 6):
        test = int(''.join([str(d) for d in combi]))
        if test >= L and test <= H:
            if all([test % int(d) == 0 for d in str(test)]):
                safe_combis += 1
    return safe_combis


def test_1():
    assert heirsdilemma(123864, 123865) == 1


def test_2():
    assert heirsdilemma(198765, 198769) == 0


def test_3():
    assert heirsdilemma(200000, 300000) == 31


if __name__ == '__main__':
    print(heirsdilemma(*list(map(int, input().split()))))
