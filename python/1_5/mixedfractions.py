# https://open.kattis.com/problems/mixedfractions

def mixed_fraction(num, denom):
    return(f"{num // denom} {num % denom} / {denom}")


def test_mf1():
    assert mixed_fraction(27, 12) == '2 3 / 12'

if __name__ == '__main__':
    while True:
        num, denom = list(map(int, input().split()))
        if num != 0 or denom != 0:
            print(mixed_fraction(num, denom))
        else:
            exit()