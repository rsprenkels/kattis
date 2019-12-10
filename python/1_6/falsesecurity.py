# https://open.kattis.com/problems/falsesecurity
import fileinput
import sys

morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--',
    ',': '.-.-',
    '.': '---.',
    '?': '----',
}


def decode(message):
    code = []
    lengths = []
    rev_lookup = {morse_code[k]: k for k in morse_code.keys()}
    for c in message:
        code.extend(morse_code[c])
        lengths.append(len(morse_code[c]))
    plaintext = []
    for l in reversed(lengths):
        one_code = ''.join([code.pop(0) for _ in range(l)])
        plaintext.append(rev_lookup[one_code])
    return ''.join(plaintext)


def test_1():
    assert decode('DSU.XFNCJEVE.OE_UJDXNO_YHU?VIDWDHPDJIKXZT?E') == 'THE_QUICK_BROWN_FOX_JUMPS_OVER_THE_LAZY_DOG'


if __name__ == '__main__':
    for line in sys.stdin:
        print(decode(line.strip()))
