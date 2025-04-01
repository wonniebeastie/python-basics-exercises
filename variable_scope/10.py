# What will the following code do and why? Don't run it until you have tried to
# answer.
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

"""
This code will print:
[10, 2, 3]

The global variable `b` can be accessed from inside the `my_function()` function
when the function is called. Index 0 is reassigned the value `10`. This mutates
the original list passed to the function. 

This is because Python uses pass-by-object-reference method of passing arguments
to functions. The reference to the original object is passed to the function, 
and whether operations performed on these objects from within functions can 
change the original or not depends on the mutability of that object. Mutable 
objects like lists can be changed.

So when the `print()` function is called with `b` as the argument, it outputs 
the newly updated value, which is `[10, 2, 3]`. 
"""
