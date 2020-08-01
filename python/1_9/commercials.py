from typing import Sequence

callcount = 0

def commercials(price: int, listeners: Sequence[int]) -> int:
    best_sum = -1000000000
    current_sum = 0
    for x in listeners:
        current_sum = max(0, current_sum + x - price)
        best_sum = max(best_sum, current_sum)
    return best_sum

def test_1():
    assert commercials(price=20, listeners=[18, 35, 6, 80, 15, 21]) == 61

if __name__ == '__main__':
    _, price = map(int, input().split())
    listeners = list(map(int, input().split()))
    print(commercials(price, listeners))