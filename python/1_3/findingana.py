def solution(line: str) -> str:
    return line[line.find('a'):]

def test_1():
    assert solution('banana') == 'anana'


def test_2():
    assert solution('polarbear') == 'arbear'


if __name__ == '__main__':
    print(solution(input()))
