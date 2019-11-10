# https://open.kattis.com/problems/lostlineup

def lineup(total, friend_list):
    output = [None] * (len(friend_list) + 1)
    output[0] = 1
    for index, friend in enumerate(friend_list):
        output[friend + 1] = index + 2
    return output


def test_lineup():
    assert lineup(4, [1,2,0]) == [1,4,2,3]


if __name__ == '__main__':
    total = int(input())
    friend_list = list(map(int, input().split()))
    print(' '.join([str(f) for f in lineup(total, friend_list)]))