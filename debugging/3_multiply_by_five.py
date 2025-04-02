# When the user inputs `10`, we expect the program to print `The result is 50!`, 
# but that's not the output we see. Why not?
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")
# Hello! Which number would you like to multiply by 5?
# 6
# The result is 66666!

def multiply_by_five2(n):
    return int(n) * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five2(number)}!")
# Hello! Which number would you like to multiply by 5?
# 6
# The result is 30!
"""
The issue was that the `input()` function returns the user input as a string.
When used with the `*` operator, it is treated as a string object, not an 
integer, so it just multiples the number of characters. 

In order to fix it, the `int()` function can be used to convert the input to
an integer so that an arithmetic operation can be performed instead of a string
operation.
"""
