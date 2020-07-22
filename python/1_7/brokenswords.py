from typing import Sequence, Tuple


def brokenswords(swords: Sequence[str]) -> Tuple[int, int, int]:
    slat_data = []
    for sword in swords:
        slat_data.append([c for c in sword])
    tb_slats = sum([1 for slat in slat_data if slat[0] == '0']) + sum([1 for slat in slat_data if slat[1] == '0'])
    lr_slats = sum([1 for slat in slat_data if slat[2] == '0']) + sum([1 for slat in slat_data if slat[3] == '0'])

    complete_swords = min(tb_slats // 2, lr_slats // 2)
    return (complete_swords, tb_slats - complete_swords  * 2, lr_slats - complete_swords * 2)

def test_1():
    assert brokenswords(['0100', '0010', '0110', '1010']) == (2, 1, 1)

if __name__ == '__main__':
    swords = []
    for _ in range(int(input())):
        swords.append(input())
    print(' '.join(map(str, brokenswords(swords))))

# from 431.5 rank 845 to 
