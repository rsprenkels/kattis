from typing import Sequence


def earlywinter(thisyear: int, prevyears: Sequence[int]) -> str:
    if all([thisyear < y for y in prevyears]):
        return "It had never snowed this early!"

    earlier = min([ndx for ndx, y in enumerate(prevyears) if y <= thisyear])
    return f"It hadn't snowed this early in {earlier} years!"

def test_1():
    assert earlywinter(2, [3,3,3,2]) == "It hadn't snowed this early in 3 years!"

def test_2():
    assert earlywinter(10, [0, 100]) == "It hadn't snowed this early in 0 years!"

def test_3():
    assert earlywinter(1, [42, 43, 44]) == "It had never snowed this early!"

if __name__ == '__main__':
    _, thisyear = map(int, input().split())
    print(earlywinter(thisyear, list(map(int, input().split()))))

# from 434.9 rank 837 to

