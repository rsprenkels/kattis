# https://open.katt is.com/problems/oddgnome

def oddgnome(gnome_list):
    for index in range(1, len(gnome_list)):
        if gnome_list[index + 1] != (1 + gnome_list[index]):
            return index + 1
    return 0


def test_1():
    assert oddgnome([7, 1, 2, 3, 4, 8, 5, 6,]) == 5


def test_2():
    assert oddgnome([5, 3, 4, 5, 2, 6,]) == 4


if __name__ == '__main__':
    num_testcases = int(input())
    for _ in range(num_testcases):
        print(oddgnome(list(map(int, input().split()))))