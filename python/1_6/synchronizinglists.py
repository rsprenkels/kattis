# https://open.kattis.com/problems/synchronizinglists

def synclist(list_1, list_2):
    sorted_1 = sorted(list_1)
    sorted_2 = sorted(list_2)
    return [sorted_2[sorted_1.index(v)] for v in list_1]


def test_1():
    assert synclist([10, 67, 68, 28, ], [55, 73, 10, 6]) == [6, 55, 73, 10]


def test_2():
    assert synclist([98, 23, 61, 49, 1, 79, 9, ], [1, 15, 32, 47, 68, 39, 24]) \
           == [68, 24, 39, 32, 1, 47, 15]


if __name__ == '__main__':
    listlen = int(input())
    while True:
        list_1 = []
        list_2 = []
        for _ in range(listlen):
            list_1.append(int(input()))
        for _ in range(listlen):
            list_2.append(int(input()))
        for res in synclist(list_1, list_2):
            print(res)
        listlen = int(input())
        if listlen == 0:
            break
        print()
