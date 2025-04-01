# What will the following code do and why? Don't run it until you have tried to
# answer.
a = 1

def my_function():
    print(a)

my_function() # 1

"""
This code will print:
1

The variable `a` is initialized in the global scope, meaning it can be accessed
from anywhere within the program. So when the function is called, the `print()`
statement executes and prints 1.
"""
