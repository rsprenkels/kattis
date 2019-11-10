def harsad(param):
    while True:
        as_string = str(param)
        sum_digits = 0
        for digit in as_string:
            sum_digits += int(digit)
        if param % sum_digits == 0:
            return param
        param += 1


def test_harsad():
    assert harsad(24) == 24
    assert harsad(25) == 27
    assert harsad(987654321) == 987654330

print(harsad(int(input())))