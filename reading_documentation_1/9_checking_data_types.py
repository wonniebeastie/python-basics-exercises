# Referring to the official Python documentation, how would you identify the
# data type of the following values?

23.5
'Call me Ishmael.'
False
0
None

print(type(23.5))                # <class 'float'>
print(type('Call me Ishmael.'))  # <class 'str'>
print(type(False))               # <class 'bool'>
print(type(0))                   # <class 'int'>
print(type(None))                # <class 'NoneType'>

"""
You can use the `type()` built-in function to tell the class/type of an object.
"""