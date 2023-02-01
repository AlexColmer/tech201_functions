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