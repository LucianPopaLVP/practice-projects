import os
import random
from art import logo, vs
from game_data import data

clear = lambda: os.system('cls')
print(logo)
score = 0
game_should_continue = True

while game_should_continue:
    def format_data(account):
        """Format the account data into printable format."""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def check_answer(guess, a_followers, b_followers):
        """Take the user guess and follower counts and returns if they got it right"""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final score: {score}")