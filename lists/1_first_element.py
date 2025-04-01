# Write a function that returns the first element of a list provided as an 
# argument. Be sure to handle the case where the input list is empty.
def first(lst):
    if lst:
        return lst[0]

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([])) # None

def first2(lst):
    return lst[0] if lst else None

print(first2(['Earth', 'Moon', 'Mars']))  # Earth
print(first2([])) # None
