import sys
from typing import Sequence

def min_max_range(values: Sequence[int]) -> (int, int, int):
    min_val = min(values)
    max_val = max(values)
    return (min_val, max_val, max_val - min_val)

for ndx, line in enumerate(sys.stdin):
    print(f"Case {ndx + 1}: ", end='')
    numbers = list(map(int, line.split()))[1:]
    result = min_max_range(numbers)
    print(' '.join(map(str, list(result))))

# from 387.1 rank 966 to 388.8 961
