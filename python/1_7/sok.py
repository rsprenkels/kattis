def sok(A: int, B: int, C: int, rA : int, rB: int, rC: int) -> (float, float, float):
    amount = min([A / rA, B / rB, C / rC])
    return (A - amount * rA, B - amount * rB, C - amount * rC)

assert sok(10, 10, 10, 3, 3, 3) == (0.0, 0.0, 0.0)

assert sok(9, 9, 9, 3, 2, 1) == (0.0, 3.0, 6.0)

A, B, C = list(map(int, input().split()))
rA, rB, rC = list(map(int, input().split()))

for v in sok(A, B, C, rA, rB, rC):
    print(v, end=' ')
print()

# from 379.0 rank 994 to 380.7 rank 985
