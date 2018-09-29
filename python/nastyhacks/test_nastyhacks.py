from unittest.mock import patch

def nastyhacks():
    num_of_tests = int(input())
    for _ in range(num_of_tests):
        revenue, expected_revenue, cost = list(map(int, input().split(' ')))
        if expected_revenue - cost > revenue:
            print('advertise')
        elif expected_revenue - cost < revenue:
            print('do not advertise')
        else:
            print('does not matter')

def test_nastyhacks(capsys):
    input = [
        '3',
        '0 100 70',
        '100 130 30',
        '-100 -70 40'
    ]

    with patch('builtins.input', side_effect=input):
        nastyhacks()
    out, err = capsys.readouterr()

    assert out.split('\n')[:-1] == [
        'advertise',
        'does not matter',
        'do not advertise']

