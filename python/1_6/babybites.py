from typing import Sequence

def babybites(N: int, words: Sequence[str]) -> str:
    if len([w for ndx, w in enumerate(words) if w == 'mumble' or int(w) == ndx + 1]) == N:
        return 'makes sense'
    else:
        return 'something is fishy'

def test_1():
    assert babybites(N=5, words=['1', '2', '3', 'mumble', '5']) == 'makes sense'

def test_2():
    assert babybites(N=8, words=['1', '2', '3', 'mumble', 'mumble', '7', 'mumble', '8',]) == 'something is fishy'

if __name__ == '__main__':
    N = int(input())
    words = input().split()
    print(babybites(N, words))

# 385.5 rank 971 to 387.1 rank 966
