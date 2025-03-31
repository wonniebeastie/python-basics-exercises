# Use Python's string methods on the string 'Captain Ruby' to create a string 
# with the value 'Captain Python'.

# Solution with `replace()` string method
print('Captain Ruby'.replace('Ruby', 'Python'))

# Solution using slicing
captain = 'Captain Ruby'
print(captain[:8] + 'Python')

# Solution using the `split()` & `join()` string methods
captain = 'Captain Ruby'.split()
captain[1] = 'Python'
print(' '.join(captain))
