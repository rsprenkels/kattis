import math


def decode(message):
    rows = []
    size = int(math.sqrt(len(message)))
    for i in range(size):
        rows.append(message[i * size: (i+1) * size])
    output = []
    for r in reversed(range(size)):
        for c in range(size):
            output.append(rows[c][r])
    return ''.join(output)

def test_1():
    assert decode("eedARBtVrolsiesuAoReerles") == "RosesAreRedVioletsAreBlue"
    assert decode("RSTEEOTCP") == "TOPSECRET"

if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        print(decode(input()))