# Your friends just showed up! Given the following list of names, use a for 
# oop to greet each friend individually.
friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends:
    print(f'Hello, {friend}!')

# Hello, Sarah!
# Hello, John!
# Hello, Hannah!
# Hello, Dave!

"""
The f-string can be used to perform string interpolation, which is a way to 
embed expressions or variables inside of string literals. Here, we use it to
embed the loop variable, `friend`, into the f-string `f'Hello, {friend}!'` on
line 6. 

So in each iteration of the `for` loop, it will be printed with the appropriate
element embedded inside.

"""
