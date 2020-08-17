from typing import Sequence, Tuple, Set, Dict


def buttonbashing(buttons: Sequence[int], target: int) -> Tuple[int, int]:
    seen: Dict[int, int] = {0: 0}
    Q = [(0, 0)]
    solution = None
    while Q:
        value, clicks = Q.pop(0)
        for reachable in [value + button for button in buttons]:
            reachable = min(max(reachable, 0), 3600)
            if reachable not in seen or seen[reachable] > clicks + 1:
                seen[reachable] = clicks + 1
                Q.append((reachable, clicks + 1))
    cook_time = min(k for k in seen.keys() if k >= target)
    return (seen[cook_time], cook_time - target)

def test_2():
    assert buttonbashing([20], 50) == (3, 10)

def test_3():
    assert buttonbashing([-10, 10, 60], 50) == (2, 0)

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        _, target = map(int, input().split())
        buttons = list(map(int, input().split()))
        result = buttonbashing(buttons, target)
        print(f'{result[0]} {result[1]}')

# from 523.7 rank 669 (team 286.4 rank 131)
