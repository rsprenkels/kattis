from functools import reduce
from itertools import combinations
from typing import Sequence, Tuple


def perket(ingredients: Sequence[Tuple[int, int]]) -> int:
    best = 1000000000000000000
    for num_ingredients in range(1, len(ingredients) + 1):
        for c in combinations(ingredients, num_ingredients):
            sour = reduce(lambda a,b : a*b, [x[0] for x in c])
            bitter = reduce(lambda a,b : a+b, [x[1] for x in c])
            best = min(best, abs(sour - bitter))
    return best

def test_1():
    assert perket([(3,10)]) == 7

def test_2():
    assert perket([(1, 7), (2,6), (3, 8), (4, 9)]) == 1


if __name__ == '__main__':
    num_ingredients = int(input())
    ingredients = []
    for _ in range(num_ingredients):
        ingredients.append(tuple(map(int, input().split())))
    print(perket(ingredients))

# from 519.8 rank 673 (team 285.4 rank 132)