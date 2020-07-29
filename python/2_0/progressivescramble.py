def to_numval(s: str) -> int:
    if s[0] == ' ':
        return 0
    else:
        return ord(s[0]) - ord('a') + 1

def to_symbol(v: int) -> str:
    if v == 0:
        return ' '
    else:
        return chr(v + ord('a') - 1)

def encrypt(m: str) -> str:
    cipher = []
    for ndx, letter in enumerate(m):
        numval = to_numval(letter)
        if ndx > 0:
            numval += cipher[-1]
        cipher.append(numval)
    return ''.join([to_symbol(numval % 27) for numval in cipher])

def decrypt(m: str) -> str:
    plain = []
    num_vals = []
    for ndx, letter in enumerate(m):
        numval = to_numval(letter)
        if ndx > 0:
            code = numval - num_vals[-1]
        else:
            code = numval
        num_vals.append(numval)
        plain.append((code + 27) % 27)
    return ''.join([to_symbol(p) for p in plain])

def test_encrypt():
    plain = 'the quick brown fox jumps over the lazy dog'
    cipher = 'taffwqzbmmofuqddjyvvezlatthchzzs eeqrqoosgn'

    assert encrypt(plain) == cipher

def test_decrypt():
    plain = 'the quick brown fox jumps over the lazy dog'
    cipher = 'taffwqzbmmofuqddjyvvezlatthchzzs eeqrqoosgn'

    assert decrypt(cipher) == plain

if __name__ == '__main__':
    for _ in range(int(input())):
        case = input()
        if case[0] == 'e':
            print(encrypt(case[2:]))
        else:
            print(decrypt(case[2:]))

# from 464.6 rank 774 to 466.6 rank 768