from unittest.mock import patch


def run_problem() -> str:
    line: str = input()
    parts = line.split(' ')
    seen = {}
    for part in parts:
        if part in seen:
            return 'no'
        else:
            seen[part] = True
    return 'yes'


def test_the_problem():
    with patch('builtins.input', side_effect=['this is the input with this in it']):
        assert run_problem() == 'no'

    with patch('builtins.input', side_effect=['this is the input']):
        assert run_problem() == 'yes'


if __name__ == '__main__':
    print(run_problem())
