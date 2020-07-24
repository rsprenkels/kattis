from typing import Sequence

def find_n_for_fraction(frac: Sequence[int]) -> int:
    # need to climb UP in the tree, start at target node, climb up to root
    p, q = frac
    n_queue = []
    while p != 1 or q != 1:
        # find the node above me
        if p - q > 0:
            # we were at a right node
            p = p - q
            n_queue.append('R')
        else:
            # we were at a left node
            q = q - p
            n_queue.append('L')
    n = 1
    while n_queue:
        if n_queue.pop() == 'L':
            n = n * 2
        else:
            n = n * 2 + 1
    return n

def test_find_n_1():
    assert find_n_for_fraction([5, 2]) == 11

def test_find_n_2():
    assert find_n_for_fraction([2178309, 1346269]) == 1431655765

if __name__ == '__main__':
    for _ in range(int(input())):
        ds, fraction = input().split()
        p, q = map(int, fraction.split('/'))
        print(f'{ds} {find_n_for_fraction([p, q])}')

# needed https://www.geeksforgeeks.org/nth-rational-number-in-calkin-wilf-sequence/ to solve it

# from 443.9 rank 820 to 445.4 rank 814
