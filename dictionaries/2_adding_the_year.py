# Add some code below the following code to define a year key with a value of 
# 2003. Don't update the dictionary literal; instead, add some code after 
# lines 1-5:

# Solution 1
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car['year'] = 2003
print(car) # {'type': 'sedan', 'color': 'blue', 'mileage': 80000, 'year': 2003}

"""
This solution uses direct key assignment to add a new key-value pair.
"""

# Solution 2
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car.setdefault('year', 2003)
print(car) # {'type': 'sedan', 'color': 'blue', 'mileage': 80000, 'year': 2003}

"""
This solution uses the `.setdefault()` dictionary method, which can be used to
add a key-value pair to a dictionary if the specified key/value does not exist.
"""

# Solution 3
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car.update({'year': 2003})
print(car) # {'type': 'sedan', 'color': 'blue', 'mileage': 80000, 'year': 2003}

"""
This solution uses the `.update()` dictionary method, which actually merges 
another dictionary to the dictionary it is called on. In this case, a
dictionary with a single key-value pair was used to merge with the original
dictionary, `car`.
"""

# Solution 4
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car |= {'year': 2003}
print(car) # {'type': 'sedan', 'color': 'blue', 'mileage': 80000, 'year': 2003}

"""
This solution uses the update operator `|=`, which achieves the same thing as
the `.update()` dictionary method.
"""
