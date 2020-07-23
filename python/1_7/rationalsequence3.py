
def nthRational(n: int, frac):
    if n > 0:
        nthRational(int(n / 2), frac)

    frac[~n & 1] += frac[n & 1]
    return frac

def test_1():
    assert nthRational(1431655765, [0, 1]) == [2178309, 1346269]

if __name__ == '__main__':
    for _ in range(int(input())):
        ds, n = map(int, input().split())
        result = nthRational(n, [0, 1])
        print(f'{ds} {result[0]}/{result[1]}')

# needed https://www.geeksforgeeks.org/nth-rational-number-in-calkin-wilf-sequence/ to solve it

# from 442.1 rank 827 to 443.8 rank 821
