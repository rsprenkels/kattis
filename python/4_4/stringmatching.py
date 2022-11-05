import sys
from typing import List, Tuple

def solution(pattern: str, text: str) -> str:
    locations = []
    search_from = 0
    while (found_at := text.find(pattern, search_from)) != -1:
        locations.append(found_at)
        search_from = found_at+1
    return ' '.join((str(x) for x in locations))

def test_1():
    assert solution('p', 'Popup') == '2 4'

if __name__ == '__main__':
    while first_line := sys.stdin.readline().rstrip('\n'):
        second_line = sys.stdin.readline().rstrip('\n')
        print(solution(first_line, second_line))