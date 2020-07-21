from typing import Sequence

"""
Getting a business permit in Kafkatown requires a trip to City Hall. There you are given a permit form that must be signed by K city clerks whose names are printed at the bottom of the form.

Entering the clerks’ room, you find a long line of people working their way down a narrow aisle along the clerks’ desks. Their desks are arranged in increasing numeric order. The aisle is so narrow that the line is forced to shuffle forward, single file, past each of the clerks’ desk in turn. Once in the line you cannot leave, back up, or change positions with other people.

As you present your permit for a signature, you are told that no clerk will sign unless all of the signatures above his or her name on the permit form have already been filled in. To your dismay, the clerks’ desks are not arranged in the same order as the names on your form.

How many times do you need to pass through the line until you can get your permit?

The first line of input contains an integer K, the number of signatures you need to collect (1≤K≤100).

This is followed by K lines of input, each containing an integer in the range 1…100, indicating the desk numbers of each of the clerks whose signature you need, in the order that they appear on your form. (Clerks whose signatures are not needed on your form are omitted from this list.)
"""

def kafkaesque(signatures: Sequence[int]) -> int:
    passes = 0
    while len(signatures) > 0:
        passes += 1
        last_popped = signatures.pop(0)
        while len(signatures) > 0 and signatures[0] > last_popped:
            last_popped = signatures.pop(0)
    return passes

def test_1():
    assert kafkaesque([1, 23, 18, 13, 99]) == 3
    assert kafkaesque([11, 20, 33, 40, 55]) == 1

if __name__ == '__main__':
    signatures = []
    for _ in range(int(input())):
        signatures.append(int(input()))
    print(kafkaesque(signatures))

# from 426.6 rank 861 to 428.3 rank 853
