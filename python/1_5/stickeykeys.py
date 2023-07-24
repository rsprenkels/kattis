# https://open.kattis.com/problems/stickykeys
def solution(line: str) -> str:
    return ''.join([c for ndx, c in enumerate(line) if ndx == 0 or (ndx > 0 and line[ndx] != line[ndx-1])])


def test_1():
    assert solution('UAAAAAPC') == 'UAPC'


if __name__ == '__main__':
    print(solution(input()))