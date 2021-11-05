import random
from game_data import data
from art import logo, vs
import os

clear = lambda: os.system('cls')


def get_random_data(data_list):
    return random.choice(data_list)


def compare_choices(a, b, choice):
    if (a["follower_count"] > b["follower_count"]) and choice == 'A':
        return True
    elif (b["follower_count"] > a["follower_count"]) and choice == 'B':
        return True
    else:
        return False


def header_screen(indicator):
    clear()
    print(logo)
    print(indicator)


def game():
    score = 0
    indicator = ""
    is_wrong = False
    a = get_random_data(data)
    b = get_random_data(data)
    while not is_wrong:
        header_screen(indicator)
        a = b
        b = get_random_data(data)
        while (a == b):
            b = get_random_data(data)

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        choice = ""
        while not (choice == 'A' or choice == 'B'):
            choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        is_correct = compare_choices(a, b, choice)
        if is_correct:
            score += 1
            indicator = f"You're right! Current score: {score}."
        else:
            is_wrong = True
            indicator = f"Sorry, that's wrong. Final score: {score}"
            header_screen(indicator)


game()