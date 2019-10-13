num_testcases = int(input())

for testcase in range(num_testcases):
    first_line = input()
    second_line = input()

    print(first_line)
    print(second_line)
    for i, char in enumerate(first_line):
        if second_line[i] == char:
            print(".", end='')
        else:
            print("*", end='')
    print()
    print()