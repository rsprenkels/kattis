import copy
from typing import Sequence

class Ingredient():
    def __init__(self, name: str, weight: float, percentage: float):
        self.name = name
        self.weight = weight
        self.percentage = percentage

class Recipe():
    def __init__(self, portions: int, desired: int, ingredients: Sequence[Ingredient]):
        self.portions = portions
        self.desired = desired
        self.ingredients = ingredients

def scale(recipe: Recipe) -> Recipe:
    main_ingredient = [ingredient for ingredient in recipe.ingredients if ingredient.percentage == 100.0][0]
    main_weight = main_ingredient.weight * recipe.desired / recipe.portions
    scaled = copy.deepcopy(recipe)
    for ingredient in scaled.ingredients:
        ingredient.weight = main_weight * ingredient.percentage / 100.0
    return scaled

def test_scale():
    r = Recipe(portions=4, desired=20)
    r.ingredients.append(Ingredient('oliveoil', 50.9, 11.2))
    r.ingredients.append(Ingredient('garlic', 12.0, 2.7))
    r.ingredients.append(Ingredient('beef', 453.6, 100.0))
    scaled = scale(r)
    print(scaled)
    assert scaled.ingredients[2].name == 'beef'
    assert scaled.ingredients[2].weight == 453.6 * 20 / 4

if __name__ == '__main__':
    for case_no in range(int(input())):
        num_ingredients, portions, desired = map(int, input().split())
        r = Recipe(portions=portions, desired=desired, ingredients=[])
        for _ in range(num_ingredients):
            name, weight, percentage = input().split()
            r.ingredients.append(Ingredient(name, float(weight), float(percentage)))
        print(f'Recipe # {case_no + 1}')
        for ingredient in scale(r).ingredients:
            print(f'{ingredient.name} {ingredient.weight:.1f}')
        print('-' * 40)

# backported from python 3.8 to python 3.6.9
# from 445.4 rank 814 to 447.2 rank 810
