from typing import Sequence


def notamused(lines: Sequence[str]) -> Sequence[str]:
    day = 1
    output = []
    while lines:
        enter_time = dict()
        exit_time = dict()
        lines.pop(0)
        while lines[0] != 'CLOSE':
            event = lines.pop(0)
        output.append(nextline)
    return output


def test_1():
    lines = """
OPEN
ENTER Sam 0
ENTER Alice 15
EXIT Sam 20
EXIT Alice 700
CLOSE
OPEN
ENTER Sam 5
ENTER Alice 10
EXIT Sam 20
EXIT Alice 35
ENTER Sam 700
EXIT Sam 710
CLOSE    
"""[1:-1].split('\n')

    expected = """
Day 1
Alice $68.50
Sam $2.00

Day 2
Alice $2.50
Sam $2.50
"""[1:-1].split('\n')

    assert notamused(lines) == expected

