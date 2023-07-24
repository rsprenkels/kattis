def solution(ann: str, ben: str) -> str:
    return ''.join(sorted(list(ann)+list(ben)))


def test_1():
    assert solution('ahjmnoy', 'acijjkll') == 'aachijjjkllmnoy'


if __name__ == '__main__':
    print(solution(input(), input()))


