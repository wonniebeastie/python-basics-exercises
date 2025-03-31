# The code provided below randomly initializes random_number to either 0 or 1 
# each time it is executed.

# Write an if statement that prints Yes! if random_number is 1, and No. if 
# random_number is 0.abs
import random
random_number = random.randint(0, 1)

if random_number:
    print('Yes!')
else:
    print('No.')

"""
We can use just the variable name `random_number` as the conditional expression
for the `if` statement in this code because it will print `'Yes!'` if the value
assigned to `random_number` on line 7 is `1` (which is a truthy value), and
`'No.'` if it is `0` (which is a falsy value). 
"""
