def get_sums(n):
    positive = sum(range(n + 1))
    odd = sum(range(1, n * 2, 2))
    even = sum(range(2, n * 2 + 2, 2))
    return positive, odd, even

assert get_sums(1) == (1, 1, 2)
assert get_sums(10) == (55, 100, 110)

data_sets = int(input())
for _ in range(data_sets):
    data_set, n = list(map(int, input().split()))
    print(f"{data_set} {' '.join(map(str, get_sums(n)))}")
