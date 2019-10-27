N = int(input())

cups = {}

for cup in range(N):
    first, second = input().split()
    if str.isdecimal(first):
        cups[int(first) / 2] = second
    else:
        cups[int(second)] = first

for radius in sorted(cups.keys()):
    print(cups[radius])
