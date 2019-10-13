name = input()

lastchar = ''

for char in name:
    if char != lastchar:
        print(char, end='')
        lastchar = char
print