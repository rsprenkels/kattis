def possible(a: int, b: int, c: int, n: int) -> str:
    if any(p == 0 for p in [a,b,c]):
        return 'NO'
    if a + b + c >= n and n >= 3:
        return 'YES'
    return 'NO'

assert possible(0, 3, 3, 5) == 'NO'
assert possible(4, 10, 6, 13) == 'YES'

if __name__ == '__main__':
    print(possible(*list(map(int, input().split()))))

# from 408.0 rank 912 to 409.7 rank 908
