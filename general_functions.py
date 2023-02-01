# Functions

# def print_something():
#     print("Something has been printed")
#
#
# print_something()

# Functions and arguments

# def print_something(print_string):
#     print(print_string)
#
# print_something("this is my variable")

# def greetings(name):
#     print("Hello, my name is " + name)

# greetings("Alex")

# return statement
# def addition(int1, int2):
#     return int1 + int2

# print(addition(2, 2))

# deafult arguments

# def addition(int1=5, int2=5):
#     return int1 + int2

# print(addition())
# print(addition(10, 10))
# print(addition())

# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Type hints

def greeting(name: str):
    print("Hello, my name is " + name)


greeting("Alex")

# def division(num1: int = 5, num2: int = 2) -> float:
#     return num1 / num2
#
#
# print(division())

# best practices
# name functions clearly using lower case and underscores
# All arguments should be clear in their need and were possible include there expected type
# remember the return statement or functiosn will return none
