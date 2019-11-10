# https://open.kattis.com/problems/numberfun

def possbile(a, b, c):
    if a + b == c  or a - b == c or  a * b == c:
        return True
    if a // b == c and a % b == 0:
        return True
    return False

def numberfun(a, b, c):
    if possbile(a,b,c) or possbile(b,a,c):
        return 'Possible'
    return 'Impossible'


def test_numberfun():
    assert numberfun(1, 2, 3) == 'Possible'

if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        a, b, c = list(map(int, input().split()))
        print(numberfun(a, b, c))