def even(number):
    return number % 2 == 0


def split_integer(parts):
    alice = sum([p for ndx, p in enumerate(sorted(parts, reverse=True)) if even(ndx)])
    bob = sum(parts) - alice
    return alice, bob

assert split_integer([3, 1, 2]) == (4, 2)
assert split_integer([1, 2, 2, 1]) == (3, 3)

_ = input()
parts = list(map(int, input().split()))
print(' '.join(map(str, split_integer(parts))))
