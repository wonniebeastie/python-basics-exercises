# What will the following code do and why? Don't run it until you have tried to
# answer.
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

"""
This code will result in an error. 

Inside the `my_function()` function, Python sees that a variable is being
assigned a value on line 6. The presence of the assignment operator (`=`) 
without a `global` keyword means that Python is treating `x` as a local
variable.

But because the right side of the assignment, `x + 5`, is attempting
to use a local `x` before `x` has been initialized (given a value) within the
local scope, we get an error.
"""
