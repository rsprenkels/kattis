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

def game_result(game: str) -> str:
    if Throw(game[:2]) > Throw(game[2:]):
        return 'Player 1 wins.'
    elif Throw(game[:2]) < Throw(game[2:]):
        return 'Player 2 wins.'
    else:
        return 'Tie.'

def test_mia1():
    assert game_result('1213') == 'Player 1 wins.'
    assert game_result('3321') == 'Player 2 wins.'
    assert game_result('6644') == 'Player 1 wins.'
    assert game_result('6511') == 'Player 2 wins.'
    assert game_result('4224') == 'Tie.'

if __name__ == '__main__':
    while True:
        game = input().replace(' ', '')
        if game == '0000':
            break
        print(game_result(game))

# from 404.2 rank 921 to 406.3 rank 920
