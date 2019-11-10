# https://open.kattis.com/problems/jobexpenses

input()

expenses = list(map(int, input().split()))

print(-sum([e for e in expenses if e < 0]))