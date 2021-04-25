import art
import os

from game_data import data
from random import randint
from sys import exit


def get_comp(data_set):
    """Select competator from data list"""

    idx = randint(1, len(data_set)) - 1

    return data_set[idx]


def clear_screen():

    if os.name == 'nt':
        cmd = 'cls'
    else:
        cmd = 'clear'

    os.system(cmd)


def get_player_choice():
    """Get player's choice"""

    choice = ""

    while choice not in ["a", "b"]:
        choice = input("Who has more followers? (A/B):  ").lower()

    return choice


def get_max(a, b):
    """Return a or b for choice with most followers"""

    if a["follower_count"] > b["follower_count"]:
        return "a"

    return "b"


def end_game(score):
    """End screen / play again?"""

    clear_screen()

    print(art.logo)
    print(f"Sorry, that's wrong.  Final score:  {score}")
    print("\n\n")

    again = ""

    while again not in ['y', 'n', 'yes', 'no']:
        again = input("Would you like to play again?  (Y/N)  ").lower()

    if again[0] == 'y':
        play_game()

    exit(0)


def play_game():
    """Main game loop"""

    score = 0
    wrong_ans = False

    choice_A = get_comp(data)
    choice_B = choice_A

    while not wrong_ans:

        while choice_A == choice_B:
            choice_B = get_comp(data)

        most_followers = get_max(choice_A, choice_B)

        clear_screen()
        print(art.logo)

        print()
        if score > 0:
            print(f"Your're right!  Current score:  {score}.")

        print(f"Compare A:  {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}.\n")

        print(art.vs)

        print(f"Compare B:  {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}.\n")

        player_choice = get_player_choice()

        if player_choice == most_followers:
            score += 1
            choice_A = choice_B
        else:
            end_game(score)


if __name__ == "__main__":

    play_game()
