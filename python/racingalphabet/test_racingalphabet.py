import math
from unittest.mock import patch


class Ring:
    def __init__(self):
        self.ring = []
        for c in range(ord('A'), ord('Z') + 1):
            self.ring.append(chr(c))
        self.ring.append(" ")
        self.ring.append("'")

    def distance(self, char_from : str, char_to: str) -> int:
        pos_from = self.ring.index(char_from)
        pos_to = self.ring.index(char_to)
        direct_dist = abs(pos_from - pos_to)
        return min(direct_dist, 28 - direct_dist)

def racingalphabet_logic(aphorism: str) -> float:
    r = Ring()
    radius = 30 # feet
    speed = 15 # feet per second
    time_1sector = ((2 * math.pi) / 28.0 * radius) / speed
    total_time = len(aphorism)
    for index in range(len(aphorism) - 1):
        # print("checking index {} of {}".format(index, len(aphorism)))
        total_time += r.distance(aphorism[index], aphorism[index + 1]) * time_1sector
    return float(total_time)

def racingalphabet():
    players = int(input())
    for player in range(players):
        aphorism: str = input()
        print("{:3.10f}".format(racingalphabet_logic(aphorism)))

def test_1():
    assert racingalphabet_logic("WINNING ISN'T EVERYTHING IT'S THE ONLY THING") == 187.6156641641

def test_2():
    assert racingalphabet_logic("WINNERS DON'T WAIT FOR CHANCES THEY TAKE THEM") == 190.4108599662

def test_racingalphabet(capsys):
    input = [
        '1',
        "WINNING ISN'T EVERYTHING IT'S THE ONLY THING"
    ]

    with patch('builtins.input', side_effect=input):
        racingalphabet()

    out, err = capsys.readouterr()

    assert out.split('\n')[:-1] == [
        '187.6156641641'
    ]


def test_ring1():
    r = Ring()
    assert r.ring[3] == 'D'
    assert r.distance("B","C") == 1
    assert r.distance("C","B") == 1
    assert r.distance("X","X") == 0
    assert r.distance("A","D") == 3
    assert r.distance("A","Z") == 3

