# Using the following code, select and print the value `'blue'` from the `car` 
# object:

# Solution 1
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(car['color']) # blue

"""
Direct key access is used to access the value paired with the `'color'` key.
"""

# Solution 2
car_values = list(car.values())
print(car_values[1]) # blue

"""
This solution makes use of the dictionary view object returned by the 
`.values()` dictionary method. This method returns a dynamic object which offers
a view to the current state of the dictionary's values.

The view object is converted to a list object using the `list()` constructor
to access the elements. Direct key access is used to access the value at index
1 of this list.
"""

# Solution 3
print(car.get('color')) # blue

"""
This solution uses the `.get()` dictionary method, which returns the value
associated with the specified key passed to it as an argument if it exists in
the dictionary it is called on.
"""
