# What happens if we take the list ['fish', 'and', 'chips'] and try to access 
# the element at index position 10? First try to determine what will happen by
# consulting the documentation, then verify your understanding in the Python 
# REPL.

['fish', 'and', 'chips'][10]  # IndexError: list index out of range

"""
You can use negative indices as well, but any time the element at a specified
index # does not exist, an error will be thrown.
"""