# Python lists come with a variety of built-in methods that allow for common 
# list manipulations. One such operation is determining the index of an item 
# in the list.

# Given a list:


fruits = ["apple", "banana", "cherry", "peach", "watermelon"]


# How would you determine the index of the fruit "cherry" in this list?

# Refer to the official Python documentation on lists to assist with your answer.


print(fruits.index("cherry")) # 2


"""
The `index` list method returns the first occurance of a specified value.
"""


print("cherry" in fruits) # True


"""
It's good practice to first use `in` to check whether a value exists or not in
a sequence before finding the index of it so the program doesn't throw an
error during runtime.
"""