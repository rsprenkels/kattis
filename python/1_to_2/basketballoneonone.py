def game(scores):
    board = {'A':0, 'B':0}
    for index in range(len(scores) // 2):
        player, score = scores[index * 2:(index + 1) * 2]
        board[player] += int(score)
        A,B = [board[p] for p in board]
        if A >= 11 and A - B >= 2:
            return 'A'
        if B >= 11 and B - A >= 2:
            return 'B'


def test_game():
    assert game('A2B1A2B2A1A2A2A2') == 'A'

if __name__ == '__main__':
    print(game(input()))