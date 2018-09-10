from unittest.mock import patch


def zanzibar():
    total_testcases: int = int(input())
    for case_index in range(total_testcases):
        turtles = list(map(int, input().split(' ')))
        surplus: int = 0
        for year_index in range(1, len(turtles) - 1):
            if turtles[year_index] > turtles[year_index - 1] * 2:
                surplus += turtles[year_index] - (turtles[year_index - 1] * 2)
        print(surplus)


def test_zanzibar(capsys):
    with patch('builtins.input', side_effect=['1', '1 28 72 0']):
        zanzibar()
    out, err = capsys.readouterr()
    assert out.split('\n')[:-1] == ['42']
