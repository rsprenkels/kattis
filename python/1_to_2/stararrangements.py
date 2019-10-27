S = int(input())

print(f"{S}:")
for n in range(S + 1)[2:-1]:
    if S % (n + n - 1) == 0 or S % (n + n - 1) == n:
        print(f"{n},{n - 1}")
    if S % n == 0:
        print(f"{n},{n}")
