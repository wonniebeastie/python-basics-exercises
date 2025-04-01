# What will the following code do and why? Don't run it until you have tried to
# answer.
if True:
    my_value = 20

print(my_value)

"""
This code will print:
20

`if` statements do not create their own scope in Python. So as long as the
conditional expression for them is truthy, the code in the body will execute.
In this case, it will run and the variable `my_value` will be assigned the
value `20`.

So by line 6, the `print()` function will have access to the value assigned to
`my_value`. 
"""
# What do you think will happen if we run the following code instead:
if False:
    my_new_value = 42

print(my_new_value)

"""
This will result in an error because the body of the `if` statement never 
executes due to the conditional expression on line 21 being falsy. So when the
`print()` function tries to access the value assigned to `my_new_value`, it
will not be able to, since it was never assigned a value.
"""
