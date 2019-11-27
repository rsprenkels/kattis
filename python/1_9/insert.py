# https://open.kattis.com/problems/insert
import math
from itertools import count

_ids = count(1)

class Node():

    def __init__(self, value):
        self.id = next(_ids)
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        tot = []
        tot.append(f"{self.id}:{self.value}({self.left.id if self.left is not None else '-'},{self.right.id if self.right is not None else '-'})")
        if self.left is not None:
            tot.append(f"{self.left}")
        if self.right is not None:
            tot.append(f"{self.right}")
        return ' '.join(tot)

    def permutations(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left == None and self.right is not None:
            return self.right.permutations()
        elif self.left is not None and self.right is None:
            return self.left.permutations()
        else:
            count_left = self.left.num_nodes()
            count_right = self.right.num_nodes()
            this_level = math.factorial(count_left + count_right) // (math.factorial(count_left) * math.factorial(count_right))
            return this_level * self.left.permutations() * self.right.permutations()

    def num_nodes(self):
        left = self.left.num_nodes() if self.left is not None else 0
        right = self.right.num_nodes() if self.right is not None else 0
        return 1 + left + right

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, value : int) -> None:
        if self.root == None:
            self.root = Node(value)
        else:
            here = self.root
            while True:
                if here.left is not None and value < here.value:
                    here = here.left
                    continue
                if here.right is not None and value >= here.value:
                    here = here.right
                    continue
                break
            if value < here.value:
                here.left = Node(value)
            else:
                here.right = Node(value)

    def insert_list(self, values: object):
        for value in values:
            self.insert(value)
        return self

    def permutations(self):
        if self.root is None:
            return 0
        return self.root.permutations()


    def __repr__(self):
        return f"{self.root}"




def test_1():
    tree = Tree().insert_list([3, 4, 3, 5, 4, 1, 2])
    assert tree.permutations() == 45

def test_2():
    tree = Tree().insert_list([16,8,24,4,12,20,28,2,6,10,14,18,22,26,30,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31])
    assert tree.permutations() == 74836825861835980800000

if __name__ == '__main__':
    while True:
        list_len = int(input())
        if list_len == 0:
            exit()
        values = list(map(int, input().split()))
        tree = Tree().insert_list(values)
        print(tree.permutations())

