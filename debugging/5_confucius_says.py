"""
You want to have a small script delivering motivational quotes, but with the 
following code you run into a very common error message: `TypeError: can only 
concatenate str (not "NoneType") to str`. What is the problem and how can you 
fix it?

def get_quote(person):
    if person == 'Yoda':
        'Do. Or do not. There is no try.'
    if person == 'Confucius':
        'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
"""
def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
# Confucius says:
# "I hear and I forget. I see and I remember. I do and I understand."
"""
The problem was that there was no `return` keyword explicitly used to return 
the strings.

So when the function was called, the only value that was being returned was
`None`, the default implicit return value of all functions in Python.None

The error message "TypeError: can only concatenate str (not "NoneType") to str"
was raised because strings cannot be concatenated with `None`, only other
strings.
"""
