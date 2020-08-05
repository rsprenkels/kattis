from typing import Sequence


def sosort(items: Sequence[str]) -> Sequence[str]:
    return sorted(items, key=lambda item : item[:2])


def test_1():
    assert sosort(['Mozart', 'Beethoven', 'Bach']) == ['Bach', 'Beethoven', 'Mozart']

def test_2():
    items = """
Hilbert
Godel
Poincare
Ramanujan
Pochhammmer
"""[1:-1].split('\n')

    expected = """
Godel
Hilbert
Poincare
Pochhammmer
Ramanujan
"""[1:-1].split('\n')
    assert sosort(items) == expected

if __name__ == '__main__':
    while True:
        num_items = int(input())
        if num_items == 0:
            break
        names = []
        for _ in range(num_items):
            names.append(input())
        for name in sosort(names):
            print(name)
        print()

# from 489.8 rank 722
