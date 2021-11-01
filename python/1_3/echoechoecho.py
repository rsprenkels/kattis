from typing import Sequence, Tuple, Set, Dict

def task(param: str) -> str:
    return param + ' ' + param + ' ' + param

def test_2():
    assert task('Hello') == 'Hello Hello Hello'

if __name__ == '__main__':
    line = input()
    print(task(line))

# from 558.1 rank 878 (team 309.0 rank 165)
