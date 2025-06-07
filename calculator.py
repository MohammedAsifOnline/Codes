# simple calculator
# this is a Day 14 weekly assignment

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    else:
        return "Invalid input"

# Step 1 : Number input section

print("Enter any TWO numbers to calculate:")

# input1 = float(input("Enter first number: "))
# input2 = float(input("Enter second number: "))
# actual code commented as it is re written in error handling method
# Error handling : Instead of default Value Error message --> try except <-- code added for Error response added for clean error message

while True:
    try:
        input1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        input2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Step 2:  user get educated which option for what ?

print("Select The desired operation:")
print("For Addition, Enter 1")
print("To Subtract, Enter 2")
print("To Multiply, Enter 3")
print("To Divide, Enter 4")

# Step 3 : User pick a choice of operation here

choice = input("Enter choice (1/2/3/4): ")

result = calculator(choice, input1, input2)
print("Result:", result)



