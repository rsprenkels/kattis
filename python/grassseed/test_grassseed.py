from unittest.mock import patch


def grassseed():
    price_per_area = float(input())
    num_of_lawns = int(input())
    total_area: float = 0.0
    for lawn_index in range(num_of_lawns):
        l, w = list(map(float, input().split(' ')))
        total_area += l * w
    print("{0:.7f}".format(total_area * price_per_area))


def test_grassseed(capsys):
    input = ['2', '3', '2 3', '4 5', '5 6']
    with patch('builtins.input', side_effect=input):
        grassseed()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['112.0000000']


def test_grassseed_2(capsys):
    input = ['0.75', '2', '2 3.333', '3.41 4.567']
    with patch('builtins.input', side_effect=input):
        grassseed()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['16.6796025']
