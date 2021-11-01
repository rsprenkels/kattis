from typing import Sequence, Tuple, Set, Dict

def task(photos: Sequence[Tuple[int, int]]) -> int:
    max_speed = 0
    for ndx in range(len(photos)-1):
        t1,d1 = photos[ndx+1]
        t2,d2 = photos[ndx]
        max_speed = max(max_speed, (d2-d1)//(t2-t1))
    return max_speed

def test_1():
    assert task([(0,0), (7,42)]) == 6

def test_2():
    assert task([(0,0), (5,24), (10,98), (15,222), (20,396)]) == 34

if __name__ == '__main__':
    num_lines = int(input())
    photos = []
    for _ in range(num_lines):
        photos.append(tuple(map(int, input().split())))
    print(task(photos))

# from 560.7 rank 875 (team 309.6 rank 165)
