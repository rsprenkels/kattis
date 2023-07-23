from functools import reduce
print(reduce(lambda a, b: a*b, list(map(int, input().split(' ')))))
