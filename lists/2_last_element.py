# Write a function that returns the last element of a list provided as an 
# argument. Be sure to handle the case where the input list is empty.
def last(lst):
    if lst:
        return lst[-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([])) # None

def last2(lst):
    return lst[-1] if lst else None

print(last2(['Earth', 'Moon', 'Mars']))  # Mars
print(last2([])) # None


