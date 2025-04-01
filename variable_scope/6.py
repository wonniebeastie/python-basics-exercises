# What will the following code do and why? Don't run it until you have tried to
# answer.
a = 1

def my_function():
    a = 2

my_function()
print(a)

"""
This will print:
1

Functions create local scopes in Python. So even though the `my_function()`
function was called before the `print(a)` line, the `a` inside the 
function is a completely separate variable from the `a` outside of the 
function.

Therefore, the `print()` function on line 9 only has access to the value 
assigned to the global `a`. 

"""
