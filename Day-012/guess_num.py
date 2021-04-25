import os
from random import randint
from sys import exit


def clear_screen():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_mode():
    """Get Difficulty level of the game"""

    mode = ""

    while not mode in ["easy", "hard"]:
        mode = input("Would you like an easy or hard game?  (easy / hard)\n > ").lower()

    return mode


def set_number(min_num=0, max_num=100):
    """Set the number to guess"""

    return randint(min_num, max_num)


def get_guess():
    
    while True:
        try:
            guess = int(input("Enter a number between 0 and 100\n > "))
        except:
            print("You must enter a number")
            continue

        if guess >= 0 and guess <= 100:
            return guess

        print("Number must be between 0 and 100\n")


def check_guess(number, guess):
    """Check if guess is correct.  0=Correct; -1=Low; 1=High"""

    if number == guess:
        return 0
    elif number < guess:
        return 1
    else:
        return -1


def game_end(won):
    """End of Game"""

    clear_screen()

    if won:
        print("Congratulations, you guessed the number")
    else:
        print("Too bad.  Maybe next time")

    print("\nWould you like to play again? (y/n)\n")

    while True:
        again = input(" > ").lower()
        if again[0] == "y":
            play_game()
        else:
            print("Goodbye")
            exit(0)


def game_init():
    """Initalize game paramaters"""

    max_guesses = {
            "easy": 10,
            "hard": 5
            }

    number = set_number(0, 100)

    return number, max_guesses[get_mode()]


def play_game():
    """Main Game Loop"""

    clear_screen()

    num, guesses = game_init()

    while guesses > 0:

        print(f"You have {guesses}")
        guess = get_guess()

        if check_guess(num, guess) == 0:
            game_end(True)

        clear_screen()

        if check_guess(num, guess) == -1:
            print(f"{guess} is too low\n")

        if check_guess(num, guess) == 1:
            print(f"{guess} is too high\n")

        guesses -= 1

    game_end(False)


if __name__ == "__main__":
    
    play_game()

