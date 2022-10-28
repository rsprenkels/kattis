import math

def solution(digits: str) -> str:
    return str(oct(int(digits, 2)))[2:]

def test_1():
    assert solution(' 1010') == '12'

def test_2():
    assert solution(' 11001100') == '314'

if __name__ == '__main__':
    digits = input()
    answer = solution(digits)
    print(answer)