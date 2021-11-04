from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(answer, guess):
    if guess > answer:
        print("Number is too high!")
    elif guess < answer:
        print("Number is too low!")
    else:
        print(f"Great job! The right number was {answer}!")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100! Try to guess it!")

answer = randint(1, 100)

turns = set_difficulty()
print("You have {} attempts remaining to guess the right number.")
guess = int(input("Make a guess: "))