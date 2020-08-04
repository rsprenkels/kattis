def compass(n1: int, n2: int) -> int:
    spin =  ((n2 - n1) + 720) % 360
    if spin > 180:
        return spin - 360
    else:
        return spin

def test_1():
    assert compass(315, 45) == 90

def test_2():
    assert compass(180, 270) == 90

def test_3():
    assert compass(45, 270) == -135

if __name__ == '__main__':
    print(compass(int(input()), int(input())))

# from 483.2 rank 734
