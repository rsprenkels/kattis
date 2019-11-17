# https://open.kattis.com/problems/volim

def volim(K, answers):
    player = K # we use 1 based player numbering
    remaining_time = 210
    for index, answer in enumerate(answers):
        time_used, answer_given = answer
        remaining_time -= time_used
        if remaining_time <= 0:
            return player
        if answer_given == 'T':
            player += 1
            if player == 9:
                player = 1


def test_1():
    assert volim(1, [(20, 'T'), (50, 'T'), (80, 'T'), (50, 'T'),(30, 'T')]) == 5



def test_2():
    assert volim(3, [(100, 'T'), (100, 'N'), (100, 'T'), (100, 'T'),(100, 'N'),]) == 4


if __name__ == '__main__':
    inital_player = int(input())
    num_answers = int(input())
    answers = []
    for _ in range(num_answers):
        time, answer = input().split()
        answers.append((int(time), answer))
    print(volim(inital_player, answers))