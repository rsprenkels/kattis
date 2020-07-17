
def inverse(c):
    if c == '0':
        return '1'
    else:
        return '0'

def erase(n: int, orig: str, erased: str) -> bool:
    if n % 2 == 0:
        return orig == erased
    else:
        return orig == ''.join([inverse(c) for c in erased])

assert erase(1,
    '10001110101000001111010100001110',
    '01110001010111110000101011110001') == True

assert erase(20,
    '0001100011001010',
    '0001000011000100') == False

if __name__ == '__main__':
    if erase(int(input()), input(), input()):
        print('Deletion succeeded')
    else:
        print('Deletion failed')

# from 414.7 rank 889 to 416.4 rank 877
