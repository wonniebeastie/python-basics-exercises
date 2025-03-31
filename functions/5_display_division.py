# Without running the following code, determine what it will print:
def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

"""
This will not print anything because parentheses need to be present after
the function's name on line 9 for the function to be called.
"""
