board = ['-','-','-',
         '-','-','-',
         '-','-','-']

# Global Variables
game_active = True
winner = None
current_player = 'X'

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_game():
    display_board()
    while game_active:
        # handles turn of the current player
        handle_turn(current_player)
        # check if the game has ended
        is_game_over()
        #flip to other player
        flip_player()
    # the game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')

def handle_turn(player):
    position = input(current_player +' Choose a position from 1-9: ')
    valid = False
    while not valid:
        while position not in['1','2','3','4','5','6','7','8','9']:
            position = input(current_player +' Choose a position from 1-9: ')

        position = int(position) - 1

        if board[position] == '-':
            valid= True
        else:
            print('You cant go there. Go again.')

    board[position] = player
    display_board()

def is_game_over():
    game_win()
    game_tie()
    return

def game_win():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
       winner = row_winner
    elif column_winner:
       winner = column_winner
    elif check_diagonals():
       winner = diagonal_winner
    else:
       winner = None
    return

def check_rows():
    global game_active
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_active = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_active
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_active = False
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]

def check_diagonals():
    global game_active
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    if diagonal_1 or diagonal_2:
        game_active = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

def game_tie():
    global game_active
    if '-'not in board:
        game_active = False

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

play_game()



