# Determine what the following code snippet prints. First solve it in your head
# or on paper, then run it in your Python environment to check the result.
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# 19 < 24 and (0 > 0 or 24 > 0)
# 19 < 24 and (False or True)
# 19 < 24 and True
# True and True
# True
print(is_moving) # True

# Bonus question: Do we need the parentheses in the boolean expression or could
# we have written the following?:
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
# 19 < 24 and 0 > 0 or 24 > 0
# True and False or 24 > 0
# False or 24 > 0
# False or True
# True

"""
The result for the bonus question code will still print `True`, but we do need
the parentheses because if the values were to change, such as if `braking_force`
was changed to `39` from the `19`, the results will be different.

Python's operator precedence dictates that `and` has higher precedence than
`or`, so the `and` expression will be evaluated first without parentheses.

It's always a good idea to use parentheses to inform Python & readers of your
code your intentions.
"""
