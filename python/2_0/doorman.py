from typing import List


def solution(N: int, queue: List[str]) -> int:
    m,w = 0,0
    while queue:
        if len(queue) == 1:
            if queue[0] == 'M':
                if abs(m+1-w) <= N:
                    return m + 1 + w
                else:
                    return m + w
            else:
                if abs(m-(w+1)) <= N:
                    return m + w + 1
                else:
                    return m + w
        else:
            if queue[0] == 'M' and abs(m+1-w) <= N:
                queue.pop(0)
                m += 1
            elif queue[0] == 'W' and abs(m-w-1) <= N:
                queue.pop(0)
                w += 1
            elif queue[1] == 'M' and abs(m+1-w) <= N:
                queue.pop(1)
                m += 1
            elif queue[1] == 'W' and abs(m-w-1) <= N:
                queue.pop(1)
                w += 1
            else:
                return m+w
    return m+w

def test_1():
    assert solution(1, list('MWWMWMMWM')) == 9

def test_2():
    assert solution(2, list('WMMMMWWMMMWWMW')) == 8

if __name__ == '__main__':
    N = int(input())
    queue = input()
    answer = solution(N, list(queue))
    print(answer)