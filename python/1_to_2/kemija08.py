line = input()

index = 0

while index < len(line):
    print(line[index], end='')
    if line[index] in "aeoiu":
        index += 2
    index += 1
print()