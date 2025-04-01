# What will the following code do and why? Don't run it until you have tried to
# answer.
def my_function():
    a = 1

    if True:
        print(a)

my_function()

"""
This code prints:
1

Defining a function creates a local scope in Python. Variables initialized
within them can be accessed by blocks that start in the same scope.

In this case, it only matters that the conditional expression for the `if`
statement is truthy for the `print(a)` line to execute and access the value
assigned to `a` because control structures in Python do not create their own
scopes.
"""
