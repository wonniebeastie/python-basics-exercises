# What will the following code do and why? Don't run it until you have tried to
# answer.
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

"""
This will print:
7

`my_function(a)` is called on line 8, with the value assigned to `a` passed
as an argument to the function. Inside the function, a new variable called `b`
is initialized using the `7` that was passed to it. `10` is added to it to
create a new object, `17`, which is then assigned to `b`.

When the `print()` function references `a`, it prints the value still assigned
to the global `a`, which is `7`. 
"""
