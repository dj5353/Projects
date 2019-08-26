#creating board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_still_going = True
winner = None
player = "X"

#displaying board
def display_board():
    print(board[0]+" |",board[1]+" |",board[2])
    print(board[3]+" |",board[4]+" |",board[5])
    print(board[6]+" |",board[7]+" |",board[8])

#handling players turn
def handle_turn(player):
    print(player + "turn")
    position = input("choose a position from 1-9")
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("Invalid Input! choose a position from 1-9")
    else:
        position = int(position)-1
    while board[position] != '-':
        print('you cannot overwitre choose again')
        position = input("Invalid Input! choose a position from 1-9")
    position = int(position)-1
    board[position] = player
    display_board()

#this function calls other functions
def play_game():
    display_board()

    while game_still_going:
        handle_turn(player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + "'s Won.")
    elif winner == None:
        print("it's a tie")


def check_if_game_over():
    check_if_win()
    check_if_tie()

#if any rows or cols are matched
def check_if_win():
    global winner
    row_winner = check_row()
    col_winner = check_col()
    diaoganl_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diaoganl_winner:
        winner = diaoganl_winner
    else:
        winner = None

#if any rows matches
def check_row():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

#if any cols matches
def check_col():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

#if diaoganlly matches
def check_diagonal():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]

#if no one wins
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

#change(flip) turn of the player
def flip_player():
    global  player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return


play_game()