input()

space_junk = list(map(int, input().split()))

min_junk = min(space_junk)

for day in range(len(space_junk)):
    if space_junk[day] == min_junk:
        print(day)
        exit()