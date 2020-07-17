def bus(k: int) -> int:
    if k == 1:
        return 1
    else:
        return int((bus(k-1) + 0.5) * 2)

assert bus(1) == 1
assert bus(3) == 7

if __name__ == '__main__':
    for _ in  range(int(input())):
        print(bus(int(input())))

# from 413.0 rank 903 to 414.7 rank 889
