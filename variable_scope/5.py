# What will the following code do and why? Don't run it until you have tried to
# answer.
a = 1

def my_function():
    print(a)
    a = 2

my_function()

"""
This code will result in an error.

If there is an assignment operator (`=`) anywhere inside of a function's body
without keywords like `global`, Python will assume that a variable is being
initialized from within that local scope. 

So even though the line `a = 2` is not executed until line 7, attempting to 
reference the value of `a` before that still results in an `UnboundLocalError`
because Python thinks that `a` is a local variable.
"""
