import sys


def is_special(c):
    return (ord(c) >= ord('!') and ord(c) <= ord('*')) or (ord(c) >= ord('[') and ord(c) <= ord(']'))


def escape(level: int, line: str) -> str:
    for times in range(level):
        new_line = []
        for c in line:
            if is_special(c):
                new_line.append('\\')
                new_line.append(c)
            else:
                 new_line.append(c)
        line = ''.join(new_line)
    return line

def test_1():
    assert escape(level=1, line="this is a 'test'") == "this is a \'test\'"


if __name__ == '__main__':
    try:
        while True:
            level = int(input())
            line = input()
            print(escape(level, line))
    except EOFError:
        pass

# from 504.3 rank 696 (team 279.7 rank 134)
