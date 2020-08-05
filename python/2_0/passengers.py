from typing import Sequence, Tuple


def trainpassengers(capacity: int, events: Sequence[Tuple[int, int, int]]) -> bool:
    in_train = 0
    for leave, enter, wait in events:
        if leave > in_train:
            return False
        in_train -= leave
        if enter > capacity - in_train:
            return False
        in_train += enter
        if wait > 0 and in_train < capacity:
            return False
    return in_train == 0


def test_1():
    assert trainpassengers(1, [(0, 1, 1), (1, 0, 0)]) == True

def test_2():
    assert trainpassengers(1, [(1, 0, 0), (0, 1, 0)]) == False

def test_3():
    assert trainpassengers(1, [(0, 1, 0), (1, 0, 1)]) == False

def test_4():
    assert trainpassengers(1, [(0, 1, 1), (0, 0, 0)]) == False

if __name__ == '__main__':
    events = []
    capacity, num_events = map(int, input().split())
    for _ in range(num_events):
        events.append(tuple(map(int, input().split())))
    print(['impossible', 'possible'][trainpassengers(capacity, events)])

# from 487.8 rank 727
