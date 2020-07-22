from collections import defaultdict
from typing import Sequence


def marko(words: Sequence[str], digits: str) -> int:
    t9 = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    t9_rev = {}
    for key, value in t9.items():
        for letter in value:
            t9_rev[letter] = key
    dd = defaultdict(int)
    for word in words:
        t9_code = ''.join([t9_rev[letter] for letter in word])
        dd[t9_code] += 1
    return dd[digits]

def test_1():
    assert marko(['tomo', 'mono', 'dak', ], '6666') == 1

def test_2():
    assert marko(['ja', 'la', ], '52') == 2

if __name__ == '__main__':
   words = []
   for _ in range(int(input())):
       words.append(input())
   print(marko(words, input()))

# from 436.8 rank 833 to