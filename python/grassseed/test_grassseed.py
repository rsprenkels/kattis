from unittest.mock import patch


def grass_seed():
    price_per_area = float(input())
    num_of_lawns = int(input())
    total_area: float = 0.0
    for _ in range(num_of_lawns):
        length, width = list(map(float, input().split(' ')))
        total_area += length * width
    total_price = total_area * price_per_area
    print("{0:.7f}".format(total_price))


def test_grass_seed(capsys):
    input = ['2', '3', '2 3', '4 5', '5 6']
    with patch('builtins.input', side_effect=input):
        grass_seed()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['112.0000000']


def test_grass_seed_2(capsys):
    input = ['0.75', '2', '2 3.333', '3.41 4.567']
    with patch('builtins.input', side_effect=input):
        grass_seed()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['16.6796025']
