# Without running the following code, determine what will be printed.
sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

"""
This will print:
3.99

`sale` is assigned the value `True` on line 2. 

The expression on line 3 is a ternary expression that returns the first value
if the condition is truthy or the second value if condition is falsy. 

In this code: the `not` operator flips the `True` value of `sale` to `False`.
Since `not True` is `False`, the conditional expression for the `if` statement 
is falsy, causing `admission_price` to be assigned the value `3.99`.
"""
