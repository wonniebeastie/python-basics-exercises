"""
You've been asked to implement a function called `digit_product` that takes a 
string of digits as an argument and returns the product of all the digits in 
the string.

When testing the function, you find that it returns `0`, which is not what you 
expect. Can you identify the issue and correct the code?

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 0

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0
"""
def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0

"""
The bug was that `product` was initially assigned `0`. Inside the `for` loop,
augmented assignment is used to perform the multiplication and reassign the
resulting value to `product`.

So `product *= digit` is essentially `product = product * digit`. So if the
current element in the iteration was `2`, it was `product = 0 * 2` which would
result in a `0`, and assigned to `product` again.

So by changing the `product` to `1`, the bug is fixed.
"""
