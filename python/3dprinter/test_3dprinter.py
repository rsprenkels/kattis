import math
from unittest.mock import patch


def printer_logic(statues: int) -> int:
    return math.ceil(math.log(float(statues), 2.0)) + 1


def printer():
    statues = int(input())
    print(printer_logic(statues))


def test_1(capsys):
    input = [
        '5'
    ]

    with patch('builtins.input', side_effect=input):
        printer()
    out, err = capsys.readouterr()

    assert out.split('\n')[:-1] == [
        '4']


def test_2():
    assert printer_logic(5) == 4
    assert printer_logic(1) == 1
