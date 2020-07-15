def owlandfox(N: int) -> int:
    sum_digits = sum([int(c) for c in str(N)])
    for closest_smaller in range(N-1, -1, -1):
        if sum([int(c) for c in str(closest_smaller)]) == sum_digits - 1:
            return closest_smaller
    return None

def test_1():
    assert owlandfox(30) == 20

def test_2():
    assert owlandfox(199) == 198

def test_3():
    assert owlandfox(10000) == 0

def test_4():
    assert owlandfox(1520) == 1510

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        print(owlandfox(int(input())))

# from 392.6 rank 952 to 394.3 rank 948
