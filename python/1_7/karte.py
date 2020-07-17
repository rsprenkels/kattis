from _collections import defaultdict

def karte(line: str) -> str:
    seen = set()
    per_suit = defaultdict(int)
    cards = [line[ndx:ndx+3] for ndx in range(0, len(line), 3)]
    for card in cards:
        if card in seen:
            return 'GRESKA'
        else:
            seen.add(card)
        per_suit[card[0]] += 1
    return ' '.join(map(str, [13 - per_suit[suit] for suit in 'PKHT']))

def test_karte():
    assert karte('P01K02H03H04') == '12 12 11 13'
    assert karte('H02H10P11H02') == 'GRESKA'
    assert karte('P10K10H10T01') == '12 12 12 12'

if __name__ == '__main__':
    print(karte(input()))

# from 406.3 rank 920 to 
