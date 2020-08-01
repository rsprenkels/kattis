import math
import sys
from typing import Sequence


def raggedright(lines: Sequence[str]) -> int:
    n = max([len(line) for line in lines])
    return int(sum([math.pow(n - len(line), 2) for line in lines[:-1]]))


def test_1():
    text = """
some blocks
of text line up
well on the right,
but
some don't.
"""[1:-1].split('\n')
    assert raggedright(text) == 283

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)
    print(raggedright(lines))