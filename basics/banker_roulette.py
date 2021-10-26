import random

print("Welcome to banker roullete. Let's spin to see who gets to pay the bill!")

names_string = input("Type everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay for the meal today!")

#or
#person_who_will_pay = random.choice(names)
#print(person_who_will_pay + " is going to pay the meal today!")