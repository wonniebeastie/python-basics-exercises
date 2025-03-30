# Using the code below as a starting point, write a while loop that prints the 
# elements of lst at each index and terminates after printing the last element 
# of the list.
lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

# 1
# 3
# 7
# 15

"""
`index < len(lst)` can be used as the condition for the `while` loop to continue
looping until the end of the list assigned to `lst`. The code `lst[index]` on
line 8 can be used to access the element at each index since Python lists are
zero-based. 
"""
