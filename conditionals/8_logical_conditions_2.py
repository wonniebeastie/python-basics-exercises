# Predict the output of the following code:
if True and False:
    print('Yes!')
else:
    print('No...')

"""
This code will output:
No...

The conditional expression on line 2 evaluates to a falsy value because the
logical operator `and` returns `False`. This operator returns the first falsy
value it encounters and returns the operand that was evaluated last if all
values are truthy. 

So the `else` statement executes, printing `'No...'`.
"""
