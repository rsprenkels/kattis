def rot(n: int, letter: str) -> str:
    codebook = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    return codebook[((codebook.index(letter)) + n) % len(codebook)]

def reverserot(n: int, plaintext: str) -> str:
    return ''.join([rot(n, c) for c in reversed(plaintext)])

def test_rot_1():
    assert rot(1, 'A') == 'B'

def test_rot_6():
    assert rot(3, '.') == 'C'

def test_1():
    assert reverserot(n=1, plaintext='ABCD') == 'EDCB'

def test_2():
    assert reverserot(n=3, plaintext='YO_THERE.') == 'CHUHKWBR.'

if __name__ == '__main__':
    while True:
        line = input()
        if line[0] == '0':
            break
        n, plaintext = line.split()
        print(reverserot(int(n), plaintext))

