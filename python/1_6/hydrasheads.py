# https://open.kattis.com/problems/hydrasheads

def determine_possible_moves(heads, tails):
    pass


def hydrasheads(heads, tails):
    possible_moves = determine_possible_moves(heads, tails)
    if len(possible_moves) == 0:
        return False
    else:
        for move in possible_moves:
            

def test_1():
    assert hydrasheads(3, 3) == 9


def test_2():
    assert hydrasheads(1, 1) == 3
