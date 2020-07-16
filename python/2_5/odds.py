# https://open.kattis.com/problems/odds
from functools import total_ordering
from itertools import product
import math

@total_ordering
class Throw():
    def __init__(self, throw : str):
        self.throw = ''.join(sorted(list(throw), reverse=True))

    def __lt__(self, other):
        if other.isMia():
            return not self.isMia()
        elif other.isDouble():
            if self.isMia():
                return False
            elif self.isDouble():
                return self.throw < other.throw
            else:
                return True
        else:
            if self.isMia() or self.isDouble():
                return False
            else:
                return self.throw < other.throw

    def __eq__(self, other):
        return self.throw == other.throw

    def __ne__(self, other):
        return not (self == other)

    def isMia(self):
        return self.throw == '21'

    def isDouble(self):
        return self.throw[0] == self.throw[1]

    def __repr__(self):
        return f"({self.throw})"

def player_one_wins(game: str) -> bool:
    return Throw(game[:2]) > Throw(game[2:])

def is_a_match(game: str, pattern: str) -> bool:
    return all([c == pattern[ndx] or pattern[ndx] == '*' for ndx, c in enumerate(game)])

def odds(pattern: str) -> str:
    games = []
    for game in product('123456', repeat=4):
        if is_a_match(game, pattern):
            games.append(game)
    wins = [g for g in games if player_one_wins(g)]
    n, d = len(wins), len(games)
    if n == 0:
        return '0'
    elif n == d:
        return '1'
    else:
        return f"{n // math.gcd(n, d)}/{d // math.gcd(n, d)}"

def test_odds_1():
    assert odds('**12') == '0'

def test_odds_2():
    assert odds('12**') == '17/18'

def test_odds_3():
    assert odds('1213') == '1'

def test_odds_4():
    assert odds('3121') == '0'

def test_odds_5():
    assert odds('*2*6') == '1/3'

if __name__ == '__main__':
    while True:
        pattern = input().replace(' ', '')
        if pattern == '0000':
            break
        print(odds(pattern))

# from 401.7 rank 932 to 404.2 rank 921
