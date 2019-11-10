# https://open.kattis.com/problems/luhnchecksum

def luhn(number):
    lookup = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    sum = 0
    for index in list(range(-1, -len(number)-1, -1)):
        if index % 2 == 1:
            sum += int(number[index])
        else:
            sum += lookup[int(number[index])]
    return sum % 10 == 0



def test_luhn():
    assert luhn('1234567890123411')

def test_2():
    assert luhn('999') == False

if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        if luhn(input()):
            print('PASS')
        else:
            print('FAIL')