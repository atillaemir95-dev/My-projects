import random

# The three possible choices in the game
choices = ["rock", "paper","scissors"]


def get_computer_choice():
    """Randomly picks rock paper scissors for the computer"""
    return random.choice(choices)


def get_user_choice():
    """Asks the user to type their choice and makes sure it's valid."""
    while True:
        user_input = input("Choose rock, paper, scissors: ").lower().strip()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please type rock, paper, or scissors.")

def decide_winner(user_choice, computer_choice):
    """Compares the two choices and returns the result as text."""
    if user_choice == computer_choice:
        return "It's a tie!"

  # Combinations where the user wins
    user_wins = [
        ("rock","scissors"),
        ("paper", "rock"),
        ("scissors","paper"),
    ]

    if (user_choice, computer_choice) in user_wins:
        return "You won!"
    else:
        return "Computer wins!"


def play_game():
    """Runs one full round of the game, then asks to play again."""
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"/You choose: {user_choice}")
        print(f"Computer choose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(result)

        # Update the score based on the result
        if result == "You won!":
            user_score += 1
        elif result == "Computer won!":
            computer_score += 1

        print(f"Score -> You {user_choice} | Computer: {computer_score}\n")

        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing!")
            break


# This makes sure the game only runs when you execute this file directly
if __name__ == "__main__":
    play_game()
