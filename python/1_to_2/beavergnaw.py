import math

# https://open.kattis.com/problems/beavergnaw

def calc_volume(D, d):
    vol_total = math.pi * D * D / 4.0 * D
    vol_cones = ((2 / 3) * math.pi * (D * D / 4) * D / 2) - ((2 / 3) * math.pi * (d * d / 4) * d / 2)
    vol_smallpart = math.pi * d * d / 4.0 * d
    return vol_total - vol_cones - vol_smallpart

def beavergnaw(D, volume):
    d_minvol = D
    d_maxvol = 0.0
    # print()
    v1 = calc_volume(D, 0)
    v2 = calc_volume(D, D)
    while True:
        # print(f"min {d_minvol} max {d_maxvol} ", end='')
        mid = (d_minvol + d_maxvol) / 2.0
        new_vol = calc_volume(D, mid)
        # print(new_vol)
        if abs(volume - new_vol) < 0.0000001:
            return mid
        if  new_vol < volume:
            d_minvol = mid
        else:
            d_maxvol = mid

def test_1():
    assert abs(beavergnaw(50,50000) - 30.901188723) < 0.0000001

if __name__ == '__main__':
    while True:
        D, V = list(map(int, input().split()))
        if (D,V) != (0,0):
            print(beavergnaw(D, V))
        else:
            exit()