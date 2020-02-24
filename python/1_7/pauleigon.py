# https://open.kattis.com/problems/pauleigon

def pauleigon(N, P, Q):
    relative_score = (P + Q) % (N * 2)
    if relative_score // N > 0 :
        return 'opponent'
    else:
        return 'paul'

assert pauleigon(5,3,7) == 'paul'

assert pauleigon(1,1,4) == 'opponent'

res = list(map(int, input().split()))

print(pauleigon(*res))