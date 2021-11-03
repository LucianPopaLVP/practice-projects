from art import logo
print(logo)

print("Welcome!")

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

function = operations["*"]
function(2, 3)

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
num2 = int(input("What's the second number?: "))
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
