def solution(a:int, b:int) -> str:
    return f'{a + b}'

def test_1():
    assert solution(3,4) == '7'


if __name__ == '__main__':
    input()
    numbers = map(int, input().split())
    print(solution(*numbers))
