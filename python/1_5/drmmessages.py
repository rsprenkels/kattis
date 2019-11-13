# https://open.kattis.com/problems/drmmessages

def rotation_value(text):
    return sum([ord(c) - ord('A') for c in text])


def rot_char(c, amount):
    return chr((((ord(c) - ord('A')) + amount) % 26) + ord('A'))


def rotate(text, amount):
    return ''.join([rot_char(c, amount) for c in text])


def drmmessage(cipher):
    first_half = cipher[:len(cipher) // 2]
    second_half = cipher[len(cipher) // 2:]
    first_rotated = rotate(first_half, rotation_value(first_half))
    second_rotated = rotate(second_half, rotation_value(second_half))
    result = []
    for index, c in enumerate(first_rotated):
        result.append(rotate(c, rotation_value(second_rotated[index])))
    return ''.join(result)

def test_drmmessage():
    assert drmmessage('UEQBJPJCBUDGBNKCAHXCVERXUCVK') == 'ACMECNACONTEST'

def test_2():
    assert drmmessage('EWPGAJRB') == 'ABCD'

if __name__ == '__main__':
    print(drmmessage(input()))