#https://open.kattis.com/problems/cprnummer

def solution(cpr: str) -> int:
    d = list(map(int, list(cpr.replace('-', ''))))
    return [0,1][(4*d[0] + 3*d[1] + 2*d[2] + 7*d[3] + 6*d[4] + 5*d[5] +4*d[6] + 3*d[7] + 2*d[8] + d[9]) % 11 == 0]

def test_1():
    assert solution('070761-4285') == 1

def test_2():
    assert solution('051002-4321') == 0

if __name__ == '__main__':
    cpr = input()
    result = solution(cpr)
    print(result)