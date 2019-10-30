# https://open.kattis.com/contests/wcvho8/problems/peg

board = []

board_dim = 7

for line in range(board_dim):
    board.append(input())

# board = [
#     '  ooo  ',
#     '  ooo  ',
#     'ooooooo',
#     'ooo.ooo',
#     'ooooooo',
#     '  ooo  ',
#     '  ooo  ',
# ]

pos_moves = 0

for line in range(board_dim):
    for x in range(board_dim):
        if board[line][x] == '.':
            if x >= 2 and board[line][x - 2:x] == 'oo':
                pos_moves += 1
            if x < board_dim - 2 and board[line][x + 1:x + 3] == 'oo':
                pos_moves += 1
            if line >= 2 and board[line - 2][x] == 'o' and board[line - 1][x] == 'o':
                pos_moves += 1
            if line < board_dim - 2 and board[line + 1][x] == 'o' and board[line + 2][x] == 'o':
                pos_moves += 1

print(pos_moves)
