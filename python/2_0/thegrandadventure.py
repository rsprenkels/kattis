def adventure(adv_str : str) -> bool:
    backpack = []
    for item in adv_str:
        if item in '$|*':
            backpack.append(item)
        elif item == 'b' and backpack and backpack[-1] == '$':
            backpack.pop()
        elif item == 't' and backpack and backpack[-1] == '|':
            backpack.pop()
        elif item == 'j' and backpack and backpack[-1] == '*':
            backpack.pop()
        elif item == '.':
            pass
        else:
            return False
    return len(backpack) == 0            
            
            
assert adventure('.$.b.|.t.*.j.................$$$$$bbbbb||....tt.....') == True

assert adventure('...$.$.$..*..*..*...*..|..*..b.....*******...') == False

for _ in range(int(input())):
    if adventure(input()):
        print('YES')
    else:
        print('NO')

# from 375.5 rank 1013 to 377.5 rank 1002