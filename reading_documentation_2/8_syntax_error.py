# The following code raises a `SyntaxError``:
speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')

# What does a SyntaxError indicate? Try running the above code, then use the 
# resulting error message to fix the error.
"""
When the code is executed, it returns: 
SyntaxError: expected ':'

This error is raised when a program cannot be understood by the Python
interpreter. In this case, it expected a colon after the `if` statement's
conditional expression, but it is not there, so the error was raised.
"""
