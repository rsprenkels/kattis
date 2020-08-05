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
    shortest_code = len(message)
    for combi in combi_generator(message, []):
        codebook = defaultdict(int)
        for part in combi:
            if len(part) > 1:
                codebook[part] += 1
        max_saving = max([len(k) for k in codebook.keys()])


def test_1():
    assert redrover('WNEENWEENEENE') == 10


def test_2():
    assert redrover('NSEW') == 4


def test_3():
    assert redrover('EEEEEEEEE') == 6
