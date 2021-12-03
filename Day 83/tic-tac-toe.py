# Make Board
# Set Win Conditions
# Set Tie Condition

row1 = ['_', '_', '_']
row2 = ['_', '_', '_']
row3 = ['_', '_', '_']

board = [row1, row2, row3]
print(f'{row1[0]}|{row1[0]}|{row1[0]}\n{row1[0]}|{row1[0]}|{row1[0]}\n{row1[0]}|{row1[0]}|{row1[0]}')
mark = ['X', 'O']
player = 0
while row1.count('_') > 0 or row2.count('_') > 0 or row3.count('_') > 0:
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or \
            board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or \
            board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or \
            board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or \
            board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
            board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' or \
            board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or \
            board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print('Game Over! Player 1 Wins!')
        break
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or \
            board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or \
            board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or \
            board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or \
            board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
            board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O' or \
            board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or \
            board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print('Game Over! Player 2 Wins!')
        break
    row_input = int(input('Select row(from 0 to 2): '))
    col_input = int(input('Select column(from 0 to 2): '))

    if board[row_input][col_input] == '_':
        board[row_input][col_input] = mark[player]
        if player == 0:
            player += 1
        else:
            player -= 1
    else:
        print('This area is already marked, pick a different area!')
    print(f'{row1[0]}|{row1[1]}|{row1[2]}\n{row2[0]}|{row2[1]}|{row2[2]}\n{row3[0]}|{row3[1]}|{row3[2]}')
