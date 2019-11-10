def provinces_and_gold(arg : str) -> str:
    G, S, C = map(int, arg.split())
    buy_power = G * 3 + S * 2 + C * 1
    if buy_power >= 8:
        victory_card = 'Province'
    elif buy_power >= 5:
        victory_card = 'Duchy'
    elif buy_power >= 2:
        victory_card = 'Estate'
    else:
        victory_card = None

    if buy_power >= 6:
        treasure_card = 'Gold'
    elif buy_power >= 3:
        treasure_card ='Silver'
    else:
        treasure_card = 'Copper'

    if victory_card != None:
        return f"{victory_card} or {treasure_card}"
    else:
        return treasure_card

def test_1():
    assert provinces_and_gold('0 1 0') == 'Estate or Copper'

def test_2():
    assert provinces_and_gold('2 1 0') == 'Province or Gold'

def test_3():
    assert provinces_and_gold('0 0 1') == 'Copper'

if __name__ == '__main__':
    print(provinces_and_gold(input()))