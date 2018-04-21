import filip

def test_1():
    myBoy = filip.filip()
    assert myBoy.giveLargest(1,2) == 2

def test_2():
    myBoy = filip.filip()
    assert myBoy.giveLargest(2,1) == 2

