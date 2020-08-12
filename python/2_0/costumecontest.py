from collections import defaultdict
from typing import Sequence


def costumecontest(categories: Sequence[str]) -> Sequence[str]:
    counts = defaultdict(int)
    for category in categories:
        counts[category] += 1
    win_with = min(counts.values())
    return sorted([k for k in counts.keys() if counts[k] == win_with])



def test_1():
    categories = """
ghost
mummy
witch
demon
demon
demon
demon
demon
demon
demon
"""[1:-1].split('\n')
    assert costumecontest(categories) == ['ghost', 'mummy', 'witch']


if __name__ == '__main__':
    categories = []
    for _ in range(int(input())):
        categories.append(input())
    print('\n'.join(costumecontest(categories)))

# from 506.5 rank 690 (team 280.9 rank 133)