num_datasets = int(input())

for data_set in range(num_datasets):
    sumsquares = 0
    set_no, base, n = map(int, input().split())
    keep_going = True
    while keep_going:
        digit = n % base
        sumsquares += digit * digit
        n = n // base
        keep_going = n > 0
    print(f"{set_no} {sumsquares}")
