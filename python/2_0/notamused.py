import sys
from collections import defaultdict
from typing import Sequence


def notamused(lines: Sequence[str]) -> Sequence[str]:
    day = 1
    output = []
    while lines:
        enter_time = defaultdict(list)
        exit_time = defaultdict(list)
        lines.pop(0)
        while lines[0][:5] != 'CLOSE':
            what, who, when = lines.pop(0).split()
            if what == 'ENTER':
                enter_time[who].append(int(when))
            else:
                exit_time[who].append(int(when))
        lines.pop(0)
        output.append(f'Day {day}')
        day += 1
        for name in sorted(enter_time.keys()):
            total_time = sum([exit_time[name][x] - enter_time[name][x] for x in range(len(enter_time[name]))])
            output.append(f'{name} ${total_time / 10:.2f}')
        output.append('')
    return output

# from 485.1 rank 733

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

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)
    print('\n'.join(notamused(lines)))