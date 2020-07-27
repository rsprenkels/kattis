def layers_needed(len_rol: int, each_time: int) -> int:
    layer = 1
    needed_of_rol = each_time
    while len_rol % needed_of_rol != 0:
        layer += 1
        needed_of_rol = needed_of_rol - (len_rol % needed_of_rol)
    return layer

def test_1():
    assert layers_needed(len_rol=31, each_time=6) == 4

def test_2():
    assert layers_needed(len_rol=10000000000, each_time=17) == 3

if __name__ == '__main__':
    print(layers_needed(*list(map(int, input().split()))))

# from 456.7 rank 793 to 458.5 rank 788