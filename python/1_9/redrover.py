import copy
from collections import defaultdict
from typing import Sequence


def combi_generator(message, chuncks: Sequence[str]):
    if not message:
        yield chuncks
        return
    for x in range(len(message)):
        chuncks.append(message[:x+1])
        yield from combi_generator(message[x+1:], chuncks)
        chuncks.pop()


def redrover(message: str) -> int:
    combinations = []
    best_saving = (0, '')
    for combi in combi_generator(message, []):
        codebook = defaultdict(int)
        for part in combi:
            if len(part) > 1:
                codebook[part] += 1
        savings = [((len(k) - 1) * codebook[k] - len(k), k) for k in codebook.keys()]
        if len(savings) > 0:
            cur_saving = max(savings)
            if cur_saving[0] > best_saving[0]:
                best_saving = cur_saving
    freq, code = best_saving
    return len(message) - freq * (len(code) - 1) + len(code)

def test_1():
    assert redrover('WNEENWEENEENE') == 10


def test_2():
    assert redrover('NSEW') == 4


def test_3():
    assert redrover('EEEEEEEEE') == 6


def test_4():
    assert redrover('S') == 1
    assert redrover('SS') == 2
    assert redrover('SSS') == 3


def test_5():
    assert redrover('SSSS') == 4

if __name__ == '__main__':
    print(redrover(input()))
