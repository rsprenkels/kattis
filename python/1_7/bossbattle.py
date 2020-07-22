def bossbattle(n: int) -> int:
    if n <= 3:
        return 1
    else:
        return n - 2

def test_bb():
    assert bossbattle(4) == 2
    assert bossbattle(7) == 5
    assert bossbattle(3) == 1
    assert bossbattle(1) == 1

if __name__ == '__main__':
    print(bossbattle(int(input())))

# from 429.8 rank 850 to 431.5 rank 845
