print("Welcome to Python Pizza Deliveries!")
size = input("what size of the pizza do you wamt? S, M, or L")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input('Do you want extra cheese on it? Y or N ')

bill = 0

if size == 'S':
    bill += 15.99
elif size == 'M':
    bill += 19.99
else:
    bill += 24.99

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill +=3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is ${bill}")