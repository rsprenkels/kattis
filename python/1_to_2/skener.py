R, C, zR, zC = map(int, input().split())

for row in range(R):
    line = input()
    buffer = ''
    for char in line:
        buffer += char * zC
    for output in range(zR):
        print(buffer)
