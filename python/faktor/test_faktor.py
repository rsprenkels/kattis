from unittest.mock import patch


def faktor():
    a, b = map(int, input().split())
    print(a * (b - 1) + 1)


def test_faktor(capsys):
    input = ['38 24']
    with patch('builtins.input', side_effect=input):
        faktor()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['875']


if __name__ == "__main__":
    faktor()
