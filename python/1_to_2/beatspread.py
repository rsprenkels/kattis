# https://open.kattis.com/contests/wcvho8/problems/beatspread

num_cases = int(input())

for case in range(num_cases):
    s, d = map(int, input().split())

    if (s + d) % 2 == 0 and (s - d) % 2 == 0:
        x = (s + d) // 2
        y = (s - d) // 2
        if x >= 0 and y >= 0:
            print(f"{x} {y}")
        else:
            if (s - d) % 2 == 0 and (d + s) % 2 == 0:
                x = (s - d) // 2
                y = (s + d) // 2
                if x >= 0 and y >= 0:
                    print(f"{x} {y}")
                else:
                    print('impossible')
    else:
        print('impossible')
