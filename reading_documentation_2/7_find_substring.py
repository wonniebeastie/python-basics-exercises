# Using the official Python documentation, can you determine how to check 
# whether a string contains a specific substring?
yam_yam = 'I like yams'

print('yams' in yam_yam) # True
print(yam_yam.count('yams')) # 1
print(yam_yam.find('yams')) # 7
print(yam_yam.index('yams')) #7 

"""
The `in` membership operator can be used to search for substrings in strings.

The `count()` method can be used to return how many times a non-overlapping
value occurs in a string.

The `find()` method can be used to return the index of the first occuerence of
where a substring occurs in a string. It returns `-1` when the substring cannot
be found.

The `index()` method can also be used to return the index of the first
occurence of a specified value. It raises a `ValueError` when the value cannot
be found.
"""
