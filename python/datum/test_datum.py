from unittest.mock import patch


def datum_logic(day: int, month: int) -> str:
    days = 0
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_names = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']

    for m in range(1, month):
        days += days_per_month[m - 1]
    days += day - 1
    return day_names[days % 7]


def datum():
    day, month = list(map(int, input().split(' ')))
    print(datum_logic(day, month))


def test_d1(capsys):
    input = [
        '1 1'
    ]

    with patch('builtins.input', side_effect=input):
        datum()
    out, err = capsys.readouterr()

    assert out.split('\n')[:-1] == [
        'Thursday']


def test_d2():
    assert datum_logic(1, 1) == 'Thursday'
    assert datum_logic(17, 1) == 'Saturday'
    assert datum_logic(25, 9) == 'Friday'
