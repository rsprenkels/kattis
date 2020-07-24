from typing import Sequence, Tuple


def inflation(canisters: Sequence[int]) -> Tuple[bool, float]:
    if all([helium <= balloon for balloon, helium in list(enumerate(sorted(canisters), start=1))]):
        return (True, min([helium / balloon for balloon, helium in list(enumerate(sorted(canisters), start=1))]))
    else:
        return (False, 0.0)

def test_1():
    assert inflation([6, 1, 3, 2, 2, 3]) == (True, 0.6)

def test_2():
    assert inflation([2, 2]) == (False, 0.0)

def test_3():
    assert inflation([4, 0, 2, 1, 2]) == (True, 0.0)

if __name__ == '__main__':
    _ = int(input())
    result = inflation(list(map(int, input().split())))
    if result[0]:
        print(f'{result[1]:.6f}')
    else:
        print(f'impossible')

# from 449.0 rank 806 to 450.8 rank 804
