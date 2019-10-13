from collections import defaultdict

hand = input().split(' ')

rank = defaultdict(int)

for card in hand:
    rank[card[0]] += 1

print(max(rank.values()))

