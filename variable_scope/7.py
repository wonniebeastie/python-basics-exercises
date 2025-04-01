# What will the following code do and why? Don't run it until you have tried to
# answer.
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

"""
This will output:
2

The variable `a` is initially assigned the value `1`.

When `my_function()` is called on line 9, the global variable `a` is reassigned
the value `2` using the `global` keyword. This keyword indicates to Python 
that we are referring to the global variable `a`, not a local one.

So when the `print()` function is called on line 10, it is that `2` that we are
accessing. 
"""
