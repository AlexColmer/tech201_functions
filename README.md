# Functions

Don't

Repeat  

Yourself

keeps the code simple 

```python
def print_something():
    print("Something has been printed")
 ```

### Return statement 
```python
   def addition(int1, int2):
        return int1 + int2
print(addition(2, 2)) # returns 4
```

### Default arguments 

```python
def addition(int1=2, int2=2):
    return int1 + int2

print(addition()) # also returns 4
print(addition(10, 10)) # overwrites and prints out 20
```
### Multiple arguments 
``` python
def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # prints 1-10 in a tuple
```
- Best practices
- Name functions clearly using lower case and underscores
- All arguments should be clear in their need and were possible include there expected type
- Remember the return statement or functions will return none
- Keep functions small to preserve readability 
- Use comments in functions/methods to give instructions on how to use them
- Consider using type hints to avoid type errors when running your code.

# Basic calculator 
```python
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
```
This code block here is a basic calculator. It takes the functions made for add, subtract, divide and multipy. Then puts them into the if statement which will ask you which type of calculation you want to add, subtract, divide or multiply. Then it will ask you to input two numbers then it will calculate these numbers together and out put the answer as x + a = c