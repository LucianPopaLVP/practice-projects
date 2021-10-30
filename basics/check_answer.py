import random

word_list = ['banana', 'lemon', 'apple', 'grape', 'mango']

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Match!")
    else:
        print("Wrong!")



