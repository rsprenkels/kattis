from typing import Sequence, List


def vote(votes: List[int]) -> str:
    total_votes = sum(votes)
    votes_with_index = list(zip(votes, range(1, len(votes)+1)))
    votes_with_index.sort(reverse=True)
    if votes_with_index[0][0] > total_votes / 2:
        return f'majority winner {votes_with_index[0][1]}'
    if votes_with_index[0][0] > votes_with_index[1][0]:
        return f'minority winner {votes_with_index[0][1]}'
    return 'no winner'

def test_1():
    assert vote([10, 21, 10]) == 'majority winner 2'


def test_2():
    assert vote([20, 10, 10]) == 'minority winner 1'


def test_3():
    assert vote([10, 10, 10]) == 'no winner'

if __name__ == '__main__':
    for _ in range(int(input())):
        votes = []
        for _ in range(int(input())):
            votes.append(int(input()))
        print(vote(votes))

# from 496.6 rank 713
