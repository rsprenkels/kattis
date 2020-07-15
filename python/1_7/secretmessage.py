import math

def secretmessage(message: str) -> str:
    mes_len = int(math.pow(math.ceil(math.sqrt(len(message))), 2))
    message += '*' * (mes_len - len(message))
    rowlen = math.ceil(math.sqrt(len(message)))
    result = []
    for col in range(rowlen):
        for row in range(rowlen - 1, -1, -1):
            if (c := message[row * rowlen + col]) != '*':
                result.append(c)
    return ''.join(result)

def test_2():
    assert secretmessage('iloveyoujack') == 'jeiaylcookuv'

def test_1():
    assert secretmessage('iloveyoutooJill') == 'iteiloylloooJuv'

if __name__ == '__main__':
    for num_messages in range(int(input())):
        print(secretmessage(input()))

