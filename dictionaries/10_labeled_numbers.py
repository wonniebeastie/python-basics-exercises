# Use a for loop to iterate over the numbers dictionary and print each 
# element's key/value pair.
numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}
# Expected output:
# A high number is 100.
# A medium number is 50.
# A low number is 10.

for level, number in numbers.items():
    print(f'A {level} number is {number}.')

# A high number is 100.
# A medium number is 50.
# A low number is 10.

"""
The `.items()` dictionary method returns each key/value pair as a tuple in an
iterable. You can then use tuple unpacking to extract the keys and values for
each iteration and embed them into the output string using f-strings.
"""
