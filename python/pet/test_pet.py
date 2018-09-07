from unittest.mock import patch


def pet() -> str:
    max = {'index': 0, 'value': 0}
    for contestant_index in range(5):
        grades = list(map(int, input().split(" ")))
        if sum(grades) > max['value']:
            max = {'index': contestant_index + 1, 'value': sum(grades)}
    return '{} {}'.format(max['index'], max["value"])


def test_problem():
    with patch('builtins.input', side_effect=[
        '5 4 4 5',
        '5 4 4 4',
        '5 5 4 4',
        '5 5 5 4',
        '4 4 4 5']):
        assert pet() == '4 19'


if __name__ == '__main__':
    print(pet())
