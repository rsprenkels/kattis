from typing import Sequence


def hardware(streetname: str, second_order_line:str, orderlines: Sequence[str]) -> Sequence[int]:
    digits = [0] * 10
    numbers_seen = 0
    while numbers_seen < int(second_order_line.split()[0]):
        orderline = orderlines.pop()
        if orderline[0] == '+':
            no_from, no_to, no_step = map(int, orderline[2:].split())
            for no in range(no_from, no_to + 1, no_step):
                for d in str(no):
                    digits[int(d)] += 1
                numbers_seen += 1
        else:
            for d in orderline:
                digits[int(d)] += 1
            numbers_seen += 1

    return digits


def test_1():
    assert hardware('Short street', '23 addresses', ['+ 101 125 2', '275', '+ 100 900 100']) == [23, 22, 5, 4, 1, 5, 1, 4, 1, 3]

if __name__ == '__main__':
    for _ in range(int(input())):
        digits = [0] * 10
        numbers_seen = 0
        streetname = input()
        second_order_line = input()
        while numbers_seen < int(second_order_line.split()[0]):
            orderline = input()
            if orderline[0] == '+':
                no_from, no_to, no_step = map(int, orderline[2:].split())
                for no in range(no_from, no_to + 1, no_step):
                    for d in str(no):
                        digits[int(d)] += 1
                    numbers_seen += 1
            else:
                for d in orderline:
                    digits[int(d)] += 1
                numbers_seen += 1
        print(streetname)
        print(second_order_line)
        for d in range(10):
            print(f'Make {digits[d]} digit {d}')
        tot_digits = sum(digits)
        print(f'In total {tot_digits} digit{"s" if tot_digits != 1 else ""}')


# from 494.1 rank 715 (missed 'deadline' by 92 seconds)