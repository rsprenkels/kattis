def solution(tower : str) -> str:
    parts = tower.split('()')
    return ['fix', 'correct'][parts[0]==parts[1]]

def test_1():
    assert solution('|()||') == 'fix'

if __name__ == '__main__':
    print(solution(input()))