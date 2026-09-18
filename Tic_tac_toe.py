def show_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---+---+---+")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def has_won(board, player):
    # The 8 possible winning lines (squares are numbered 0-8)
    winning_lanes = [
        (0,1,2), (3,4,5), (6,7,8),  #rows
        (0,3,6), (1,4,7), (2,5,8),  #columns
        (0,4,8), (2,3,6),           #diagonals
    ]
    for a, b, c in winning_lanes:
        if board [a] == board[b] == board[c] == player:
            return True
    return False


def play():
    board = [" "] * 9 # 9 empty squares
    player = "X"

    for move_count in range (9): # at most 9 moves can be played
        show_board(board)

        #keep asking until the player enters a valid move
        while True:
            choice = input(f"Player {player}, pick a square (1-9): ")
            if choice.isdigit() and 1 <= int(choice) <= 9:
                position = int(choice) - 1
                if board[position] == " ":
                    break
                print("That square iss taken, please pick another one (1-9)")
            else:
                print("Please enter a number between 1 and 9 ")

        board[position] = player

        if has_won(board, player):
            show_board(board)
            print(f"player {player} wins!")
            return


        #switch to the other player
        if player == "X":
            player = "O"
        else:
            player = "X"

    show_board(board)
    print("Its a draw!")


play()