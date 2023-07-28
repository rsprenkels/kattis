from typing import List, Tuple


def solution(days: List[List[int]]) -> List[int]:
    res = []
    for day in range(len(days[0])):
        d = [days[r][day] for r in range(3)]
        res.append(sorted(d)[1])
    return res

def test_1():
    assert solution([[1,2,3,4],[4,3,2,1],[2,2,2,2]]) == [2,2,2,2]


if __name__ == '__main__':
    input()
    days = []
    for _ in range(3):
        days.append(list(map(int, input().split(' '))))
    print(' '.join(map(str, solution(days))))

