from typing import List

numbers = []

get_more_lines = True

while (get_more_lines):
    line = input('give me a number: ')
    if line:
        numbers.append(int(line))
    else:
        get_more_lines = False

def own_sort(numbers: List[int]) -> List[int]:
    return sorted(numbers)

print(f'got: [{own_sort(numbers)}]')

¡1