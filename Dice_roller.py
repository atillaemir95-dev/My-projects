import random
from unittest import result


def roll_dice(number_of_dice, sides):
    result = []
    for _ in range(number_of_dice):
        result.append(random.randint(1, sides))
    return result


def ask_for_number(question, minimum, maximum):
    # Keep asking until the user enters a valid number in the allowed range
    while True:
        text = input(question)
        if text.isdigit() and minimum <= int(text) <= maximum:
            return int (text)
        print(f"Please enter a number between{minimum} and {maximum}")


print("Dice Roller")

while True:
    number_of_dice = ask_for_number("How many dice? (1-10): ", 1,10)
    sides = ask_for_number("How many sides per dice(2-100)", 2, 100)

    result = roll_dice(number_of_dice, sides)
    print("You rolled:", result)
    print("Total", sum(result))

    again = input("Roll again? (y/n)").lower().strip()
    if again != "y":
        print("Goodbye!")
        break