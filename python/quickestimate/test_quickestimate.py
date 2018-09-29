import math
from unittest.mock import patch


def quickestimate():
    num_of_tests = int(input())
    for _ in range(num_of_tests):
        estimate = int(input())
        if estimate > 0:
            print(math.ceil(math.log(float(estimate + 1), 10.0)))
        else:
            print(1)


def test_quickestimate(capsys):
    input = [
        '3',
        '0',
        '10',
        '100'
    ]

    with patch('builtins.input', side_effect=input):
        quickestimate()
    out, err = capsys.readouterr()

    assert out.split('\n')[:-1] == [
        '1',
        '2',
        '3']
