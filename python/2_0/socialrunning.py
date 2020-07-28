from typing import Sequence


def socialrunning(distances: Sequence[int]) -> int:
    return min([distances[first_runner] + distances[(first_runner - 2) % len(distances)] for first_runner in range(len(distances))])

def test_1():
    assert socialrunning([4, 1, 2, 3]) == 4

if __name__ == '__main__':
    distances = []
    for _ in range(int(input())):
        distances.append(int(input()))
    print(socialrunning(distances))

# from 461.1 rank 781 to 463.1 rank 777
