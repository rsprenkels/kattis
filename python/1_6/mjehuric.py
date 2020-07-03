from typing import Tuple, Sequence

def sorter(items: Sequence[int]):
    swaps_made = True # not really, but okay
    while swaps_made:
        swaps_made = False
        for ndx in range(len(items) - 1):
            if items[ndx] > items[ndx + 1]:
                items[ndx], items[ndx + 1 ] = items[ndx + 1],items[ndx]
                swaps_made = True
                yield items


steps = []
for step in sorter([2,3,4,5,1]):
    steps.append(step)
assert steps == [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]]

for step in sorter(list(map(int, input().split()))):
    print(" ".join([str(item) for item in step]))
    
# from 362.1 rank 1055 to 363.7 rank 1049
   