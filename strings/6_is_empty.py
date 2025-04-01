# Write a function that checks whether a string is empty or not.
def is_empty(s):
    return not s

def is_empty2(s):
    return s == ''

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

"""
The `not` keyword can be used to negate the string. If it is empty, meaning
it's a falsy value, the `not` will convert it to `True` (yes, it is empty) and
if it is not empty, meaning it's a truthy value, the `not` will convert it to
`False` (no, it is not empty).
"""

print(is_empty2('mars'))  # False
print(is_empty2('  '))    # False
print(is_empty2(''))      # True

# LS Solution
# Same as above in addition to:
def is_empty(s):
    return len(s) == 0

