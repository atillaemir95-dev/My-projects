import tkinter as tk

board = [" "] * 9  # 9 empty squares, numbered 0-8
player = "X"
game_over = False


def has_won(board, player):
    # The 8 possible winning lines
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def on_click(position):
    global player, game_over

    # Ignore clicks on taken squares or after the game has ended
    if game_over or board[position] != " ":
        return

    board[position] = player
    buttons[position].config(text=player)

    if has_won(board, player):
        status_label.config(text=f"Player {player} wins!")
        game_over = True
    elif " " not in board:
        status_label.config(text="It's a draw!")
        game_over = True
    else:
        # Switch to the other player
        if player == "X":
            player = "O"
        else:
            player = "X"
        status_label.config(text=f"Player {player}'s turn")


def reset_game():
    global player, game_over

    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ")
    player = "X"
    game_over = False
    status_label.config(text="Player X's turn")


# --- Build the window ---
window = tk.Tk()
window.title("Tic Tac Toe")

status_label = tk.Label(window, text="Player X's turn", font=("Arial", 16))
status_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    button = tk.Button(
        window,
        text=" ",
        font=("Arial", 32),
        width=4,
        height=2,
        command=lambda position=i: on_click(position),
    )
    button.grid(row=1 + i // 3, column=i % 3)
    buttons.append(button)

reset_button = tk.Button(window, text="New game", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()