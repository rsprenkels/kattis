def avion(codes):
    hitlist = [index + 1 for index, code in enumerate(codes) if 'FBI' in code]
    if len(hitlist) > 0:
        return ' '.join([str(i) for i in hitlist])
    else:
        return 'HE GOT AWAY!'


def test_avion():
    input = """N-FBI1
9A-USKOK
I-NTERPOL
G-MI6
RF-KGB1"""
    assert avion(input.split('\n')) == '1'


def test_2():
    input = """47-FBI
BOND-007
RF-FBI18
MARICA-13
13A-FBILL"""
    assert avion(input.split('\n')) == '1 3 5'


def test_3():
    input = """N321-CIA
F3-B12I
F-BI-12
OVO-JE-CIA
KRIJUMCAR1
"""
    assert avion(input.split('\n')) == 'HE GOT AWAY!'



if __name__ == '__main__':
    lines = []
    for __ in range(5):
        lines.append(input())
    print(avion(lines))