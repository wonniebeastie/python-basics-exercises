# You come across the following code. What errors does it raise for the given 
# examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

# print(find_first_nonzero_among(0, 0, 1, 0, 2, 0))
"""
This outputs:
    find_first_nonzero_among(0, 0, 1, 0, 2, 0)
TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given

A `TypeError` is raised when a value of the wrong type is used in an expression.TypeError
In this case, the function `find_first_nonzero_among()` takes only one argument
(as it has only one parameter, `numbers`) but six were given.
"""

print(find_first_nonzero_among(1))
"""
This outputs:
    for n in numbers:
TypeError: 'int' object is not iterable

For this code, the correct number of arguments were provided, but the code on
line 5 expected the argument to be an iterable (so the `for` loop can iterate
over it), not a single integer. 
"""
