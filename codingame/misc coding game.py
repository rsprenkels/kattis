import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

bits = list(''.join([f'{ord(c):07b}' for c in message]))

# print(f"bits:{bits}", file=sys.stderr, flush=True)
result = []
while bits:
    cur_bit = bits[0]
    seq_len = 0
    while bits and bits[0] == cur_bit:
        seq_len += 1
        bits.pop(0)
    # print(f"seq_len:{seq_len}", file=sys.stderr, flush=True)
    result.append(f'{"00" if cur_bit == "0" else "0"} {"0" * seq_len}')

print(' '.join(result))


# hoe werkt deze?
n=int(input())

ls=[input()for _ in "*"*n]
m=max(map(len,ls))
for l in ls:
    if all(c in 'AHIMOTUVWXY ' for c in l):
        l = l[::-1]

    print(" "*(m-len(l))+l.rstrip())