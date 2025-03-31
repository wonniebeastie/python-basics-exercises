# Let's generalize the function from the previous exercise. Implement a 
# function named cite that takes two string arguments: the author of the quote 
# and what they said. It then prints the quote, as shown below.
def cite(author, quote):
    print(f'{author} said: "{quote}"')

def cite2(author, quote):
    print(author + ' said: "' + quote + '"')

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

cite2('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

"""
You can use f-strings to perform string interpolation to embed variables into
string literals. This was the method used in the `cite()` function defined on
line 4, to embed the arguments passed to the function.

You can also achieve this using string concatenation with the `+` operator, as
exemplified in the function `cite2()`, defined on line 7.
"""
