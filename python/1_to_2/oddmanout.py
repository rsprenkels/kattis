def odd_man_out(case_no, line):
    codes = sorted(list(map(int, line.split())))
    for guest in range(0, len(codes), 2):
        if guest == len(codes) - 1 or codes[guest] != codes[guest + 1]:
            return f"Case #{case_no}: {codes[guest]}"


def test_1():
    assert odd_man_out(1, '1 2147483647 2147483647') == 'Case #1: 1'

def test_2():
    assert odd_man_out(2, '3 4 7 4 3') == 'Case #2: 7'

if __name__ == '__main__':
    for case in range(int(input())):
        input()
        print(odd_man_out(case + 1, input()))