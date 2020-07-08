from typing import Sequence
from operator import itemgetter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False    

    def mhdist(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __repr__(self):
        return f"p({self.x},{self.y})"


def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs

def word_sorter(word : str, checker_list: Sequence[str]) -> Sequence[str]:

    keyboard = [
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm',]

    let_loc = {}
    for line_index, line in enumerate(keyboard):
        for letter_index, letter in enumerate(line):
            let_loc[letter] = Point(letter_index, line_index)
    
    distances = []
    for item in checker_list:
        dist = sum([let_loc[item[ndx]].mhdist(let_loc[word[ndx]]) for ndx, letter in enumerate(word)])
        distances.append((item, dist))
    
    # multisort(distances, ((0, True), (1, False)))
    return [dist for dist in multisort(distances, ((1, False), (0, False)))]


num_testcases = int(input())
for _ in range(num_testcases):
    word, num_entries = input().split()
    entries = []
    for _ in range(int(num_entries)):
        entries.append(input())
    
    for res in word_sorter(word, entries):
        print(f"{res[0]} {res[1]}")

# from 366.8 rank 1039 to 368.7 rank 1028

