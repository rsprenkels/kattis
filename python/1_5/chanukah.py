# https://open.kattis.com/problems/chanukah

def chanukah(n):
    if n % 2 == 0:
        return (n + 1) * n // 2 + n
    else:
        return (n + 1) * (n - 1) // 2 + (n + 1) // 2 + n


def test_ch():
    assert chanukah(8) == 44


def test_odd():
    assert chanukah(3) == 9


def test_ch2():
    assert chanukah(10) == 65

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        case, days = list(map(int, input().split()))
        print(f"{case} {chanukah(days)}")