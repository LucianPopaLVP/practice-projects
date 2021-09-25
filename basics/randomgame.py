from random import randint

# generate a number 1 - 10
answer = randint(1, 10)

# imput from user
# check if imput is a number 1 - 10
# check if number is right guess. if False
# ask again

while True:
    try:
        guess = int(input('Guess a number 1 - 10:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('You are right!')
                break
        else:
            print('Read carefully! Need a number 1- 10:  ')
    except ValueError:
        print('Please enter a number!!!')
        continue

