import random
from random import randint

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are right! You little lucky cookie!')
            return True

        else:
            print('Read carefully! I requested a number 1- 10:  ')

if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number 1 - 10:  '))
            if(run_guess(guess, answer)):
                break

        except ValueError:
            print('Please enter a number!!!')
            continue

