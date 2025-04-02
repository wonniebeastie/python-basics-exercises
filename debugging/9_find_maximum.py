"""
Your colleague has implemented a custom function to find the maximum value in a
list. However, the function sometimes works correctly, but other times it 
produces incorrect results. Can you help your colleague fix the bug?

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98, outputted 98
print(find_maximum([-1, 0, 5, 3]))        # Expected 5, outputted 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2, outputted 0
"""
def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

"""
The bug was that the function did not account for an argument that was composed
entirely of negative numbers. So `max_number`, being assigned 0, would always
be greater than such an argument. 

The fixed function returns `None` if the argument is a fasly value, and if it 
is not, uses the built-in `max()` function to return the maximum value in the 
argument.
"""

# LS Solution
def find_maximum2(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum2([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum2([-1, 0, 5, 3]))         # Expected 5
print(find_maximum2([-10, -3, -20, -2]))   # Expected -2

"""
In this solution, `max_number` is initially assigned the value of the very
first element of the argument list. As the `for` loop iterates through the
argument list, it assigns the next biggest value to `max_number` and compares 
it to the number that comes after, until the list is exhausted, and returns
the largest value.
"""
