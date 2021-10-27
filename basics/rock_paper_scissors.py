rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

rsp = [rock, paper, scissors]

print("Hello, This is Rock, Paper & Scissors Game!!!")
print("0 - Rock\n1 - Paper\n2 - Scissors")

game_images = [rock, paper, scissors]

user_choice = int(input("What do You choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])
print(f"Computer chose {computer_choice}")

if user_choice >= 3 or  user_choice < 0:
    print("Invalid choice! You lost!")
elif user_choice == 0 and computer_choice == 2:
    print("You won!")
elif computer_choice == 0 and user_choice == 2:
    print("You lost!")
elif computer_choice > user_choice:
    print("You lost!")
elif user_choice > computer_choice:
    print("You won!")
elif computer_choice == user_choice:
    print("Draw!")
