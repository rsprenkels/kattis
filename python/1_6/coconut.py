class Countable():
    pass

class Hand(Countable):
    def __init__(self, player, left_right):
        self.player = player
        self.left_right = left_right
        self.state = 'o'
        
    def __repr__(self):
        return f"{self.player}-{self.left_right}:{self.state}"

    def to_next_state(self):
        if self.state == 'o':
            self.state = '_'
        elif self.state == '_':
            self.state = '.'

class Player(Countable):
    def __init__(self, player_number: int):
        self.player_number = player_number
        self.state = '()'
        self.hands = Hand(self, 'L'), Hand(self, 'R')
        
    def get_hands(self):
        if self.state == '()':
            return [self]
        else:
            return [h for h in self.hands if h.state != '.']
        
    def to_next_state(self):
        if self.state == '()':
            self.state = ''
    
    def both_hands_gone(self):
        return self.hands[0].state == '.' and self.hands[1].state == '.'
    
    def __repr__(self):
        return f"{self.player_number}:{self.state}"
    


def coconut(syllables: int, num_players: int):
    players = []
    for player_number in range(num_players):
        players.append(Player(player_number + 1))

    countable_start = players[0]
    while len(players) > 1:
        countables = []
        for p in players:
            countables.extend(p.get_hands())
        ndx_start = countables.index(countable_start)
        next_countable = (ndx_start + syllables - 1) % len(countables)
        nc = countables[next_countable]
        # print(f"countables:{countables} countable_start:{countable_start} ", end='')
        # print(f" ndx_start {ndx_start} next:{nc} ", end='')
        if nc.state == '()':
            countable_start = nc.hands[0]
        else:
            countable_start = countables[(countables.index(nc) + 1) % len(countables)]
        # print(f" new startat {countable_start}", end='')
        nc.to_next_state()
        # print(f" newstate:{nc}")
        to_be_removed = [p for p in players if p.both_hands_gone()]
        assert len(to_be_removed) <= 1
        for p in to_be_removed:
            players.remove(p)
    return players[0].player_number        



# assert coconut(syllables=10, num_players=2) == 2
assert coconut(syllables=10, num_players=10) == 7
# assert coconut(syllables=2, num_players=3) == 2

print(coconut(*list(map(int, input().split()))))
      
