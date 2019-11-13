# https://open.kattis.com/problems/eenymeeny

def eenymeeny(rhime_len, kids):
    kids_pointer = 0
    next_team = 0
    teams = [[],[]]
    while len(kids) > 0:
        kids_pointer = (-1 + kids_pointer +  rhime_len) % len(kids)
        teams[next_team].append(kids.pop(kids_pointer))
        next_team = (next_team + 1) % 2
    return tuple(teams)


def test_eenymeeny():
    assert eenymeeny(rhime_len=3, kids=['Kalle', 'Lisa', 'Alvar', 'Rakel']) == \
           (['Alvar', 'Rakel'], ['Lisa', 'Kalle'])

def test_2():
    assert eenymeeny(rhime_len=2, kids=['a', 'b', 'c']) == \
           (['b', 'c'], ['a'])

if __name__ == '__main__':
    rhime_len = len(input().split())
    num_kids = int(input())
    kids = []
    for _ in range(num_kids):
        kids.append(input())
    teams = list(eenymeeny(rhime_len, kids))
    for team in teams:
        print(len(team))
        for kid in team:
            print(kid)


