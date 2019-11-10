left, right = list(map(int, input().split()))

if left == right and left > 0:
    print(f"Even {left * 2}")
elif left == right == 0:
    print("Not a moose")
else:
    print(f"Odd {max(left, right) * 2}")