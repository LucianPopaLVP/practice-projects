from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def check_answer(answer, guess, turns):
    """checks answer against guess and returns tje numbers of turns remaining"""
    if guess > answer:
        print("Number is too high!")
        return turns - 1
    elif guess < answer:
        print("Number is too low!")
        return turns - 1
    else:
        print(f"Great job! The right number was {answer}!")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100! Try to guess it!")

    answer = randint(1, 100)
    print(f"{answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the right number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("You are out of guesses! You lost!")


game()