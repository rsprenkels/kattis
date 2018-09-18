from unittest.mock import patch


def sum_of_digits(par: str) -> int:
    total: int = 0
    for c in par:
        total += int(c)
    return total


def zamka():
    L: int = int(input())
    D: int = int(input())
    X: int = int(input())

    min_t, max_t = D + 1, L - 1

    for t in range(L, D + 1):
        if sum_of_digits(str(t)) == X:
            min_t = min(t, min_t)
            max_t = max(t, max_t)
    print(min_t)
    print(max_t)


def test_zamka(capsys):
    input = ['1', '100', '4']
    with patch('builtins.input', side_effect=input):
        zamka()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['4', '40']


if __name__ == '__main__':
    zamka()
