# Examine the code shown below. Without running it, determine what it will 
# print. If you're not sure, refer to our Python book.
animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

"""
This code will print:
neigh

The match/case statement is used to compare a single value to multiple values.
If the expression for the `match` statement is evaluated and there is a match
for that value within the `case` statements, the body of that case statement
will be executed.

There is also an optional wildcard pattern (`case _:`) at the end that can be
used as a catch-all if none of the previous cases match. 
"""
