num_temps = int(input())

temps = list(map(int, input().split()))

sub_zero = [t for t in temps if t < 0]

print(len(sub_zero))
