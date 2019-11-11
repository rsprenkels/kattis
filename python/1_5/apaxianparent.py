# https://open.kattis.com/problems/apaxianparent

def apaxianparent(Y_and_P):
    Y, P = Y_and_P.split()
    if Y[-2:] == 'ex':
        return Y + P
    elif Y[-1:] == 'e':
        return Y + 'x' + P
    elif Y[-1:] in 'aiou':
        return Y[:-1] + 'ex' + P
    else:
        return Y + 'ex' + P


def test_apaxianparent():
    assert apaxianparent('menolaxios mox') == 'menolaxiosexmox'

def test_2():
    assert apaxianparent('alemaxe maxos') == 'alemaxexmaxos'

def test_3():
    assert apaxianparent('pamoli toxes') == 'pamolextoxes'

def test_4():
    assert apaxianparent('andrex naxos') == 'andrexnaxos'

if __name__ == '__main__':
    print(apaxianparent(input()))

