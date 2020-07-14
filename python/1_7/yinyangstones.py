def yys(line: str) -> int:
    if len([c for c in line if c == 'W']) == len(line) // 2 and len(line) % 2 == 0:
        return 1
    else:
        return 0

assert yys('WWBWBB') == 1

assert yys('WWWWBBW') == 0

print(yys(input()))

# from 388.8 rank 961 to 390.5 rank 958
