import math

# lowest common multiple
def lcm(a: int, b: int) -> int:
    return a * b / math.gcd(a, b)

def blink_at_same_time(p: int, q: int, waittime: int) -> str:
    if lcm(p, q) <= waittime:
        return 'yes'
    else:
        return 'no'

def test_1():
    assert blink_at_same_time(2, 5, 20) == 'yes'

def test_2():
    assert blink_at_same_time(4, 3, 11) == 'no'

if __name__ == '__main__':
    print(blink_at_same_time(*list(map(int, input().split()))))

# from 397.7 rank 941 to 399.4 rank 937
