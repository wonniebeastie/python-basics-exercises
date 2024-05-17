# Python offers multiple ways to format strings. The str.format method is a 
# popular method, but since Python 3.6, a new way called f-strings (formatted
# string literals) was introduced. F-strings offer a concise way to embed 
# expressions inside string literals.

# Given the following variables:

name = "Victor"
profession = "programmer"

# How can you print the string Hello, Victor. You are a programmer. using the 
# str.format method? You should fill in the name and profession in a string 
# literal that contains the rest of the text.

# How can you achieve the same result using an f-string?

# Refer to the Python documentation on Format String Syntax and Formatted 
# string literals for guidance.


"""
`str.format()` method.
"""

sentence = "Hello, {name}. You are a {profession}.".format(name = "Victor", profession = "programmer")
print(sentence) # 'Hello, Victor. You are a programmer.'



"""
f-string method.
"""

sentence_f_string = f'Hello, {name}. You are a {profession}.'
print(sentence_f_string) # 'Hello, Victor. You are a programmer.'


"""
Solution for the format method was:

message_format = "Hello, {}. You are a {}."
formatted_message = message_format.format(name, profession)

print(formatted_message)
# Hello, Victor. You are a programmer.


My code was too long. I wasn't sure how to use the method.

f-strings offer a concise way to embed expressions inside strings.

"""