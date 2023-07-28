# https://open.kattis.com/problems/internationaldates
def solution(us_eu: str) -> str:
    a, b, _ = list(map(int, us_eu.split('/')))
    if a > 12:
        return 'EU'
    elif b > 12:
        return 'US'
    else:
        return 'either'


def test_1():
    assert solution('25/03/2023') == 'EU'
    assert solution('04/02/2023') == 'either'
    assert solution('07/23/1972') == 'US'


if __name__ == '__main__':
    print(solution(input()))