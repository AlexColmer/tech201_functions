# function for adding
def add(num1: int, num2: int):
    return num1 + num2


# function for subtracting
def subtract(num1: int, num2: int):
    return num1 - num2


# function for dividing
def divide(num1: int, num2: int):
    return num1 / num2


# function for dividing
def multiply(num1: int, num2: int):
    return num1 * num2


# this code will ask what you would like to do with the calculator and print out your response
choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for division, 4 for multiplication "))
num1 = int(input("Input your first number "))
num2 = int(input("Input your second number "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 3:
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == 4:
    print(num1, "*", num2, "=", multiply(num1, num2))
else:
    print("invalid option")
