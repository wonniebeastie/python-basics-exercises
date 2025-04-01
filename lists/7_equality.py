# Predict the output of the code shown below. When you run the code, do you see 
# what you expected? Why or why not?
list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2) # True

"""
I predict that this will print:
True

The equal to operator (`==`) is used to check whether two objects are equal in
value. It returns `True` if they are, and `False` if they are not. It doesn't
take into account whether they're the same object in memory.
"""
print(list1 is list2) # False
