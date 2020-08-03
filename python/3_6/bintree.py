from typing import Any


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.key}({self.left.key if self.left != None else 'N'},{self.right.key if self.right != None else 'N'})"

class Bintree:
    def __init__(self):
        self.root = None


    def insert(self, key: int, value: int):
        if self.root == None:
            self.root = Node(key=key, value=value)
        else:
            n = self.root
            while True:
                if key <= n.key and n.left != None:
                    n = n.left
                elif key > n.key and n.right != None:
                    n = n.right
                else:
                    break
            if key <= n.key:
                n.left = Node(key=key, value=value)
            else:
                n.right = Node(key=key, value=value)

    def remove(self, key: int):
        d = self.search(key=key)
        if d != None:
            pass


    def search(self, key: int):
        return self.search_recursive(None, self.root, key=key)


    def search_recursive(self, parent: Node, n: Node, key: int):
        if n == None or n.key == key:
            return n
        if key <= n.key:
            return self.search_recursive(parent=n, n=n.left, key=key)
        else:
            return self.search_recursive(parent=n, n=n.right, key=key)


    def min(self):
        if self.root == None:
            return None
        else:
            n = self.root
            while n.left != None:
                n = n.left
            return n


    def values(self):
        yield from self.generate(self.root)


    def generate(self, n: Node):
        if n.left != None:
            yield from self.generate(n.left)
        if n != None:
            yield (n.key, n.value)
        if n.right != None:
            yield from self.generate(n.right)


def test_inserts():
    t = Bintree()
    test_sequence = [19, 12, 11, 14, 13, 17, 10, 18, 15, 16]
    values = list([(v, k) for k, v in enumerate(test_sequence)])
    for k, v in values:
        t.insert(k, v)
    res1 = list(t.values())
    res2 = next(t.values())
    search_result = t.search(11)
    print(search_result)
    smallest: Node = t.min()
    assert smallest.key == 10


