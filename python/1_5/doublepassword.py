# https://open.kattis.com/problems/doublepassword
import math


def solution (pwd_1: str, pwd_2: str) -> int:
    return math.prod([2 if dig_1 != dig_2 else 1 for dig_1, dig_2 in zip(pwd_1, pwd_2)])

def test_1():
    assert solution('1111','1234') == 8

def test_2():
    assert solution('2718','2718') == 1

if __name__ == '__main__':
    pwd_1 = input()
    pwd_2 = input()
    print(solution(pwd_1, pwd_2))