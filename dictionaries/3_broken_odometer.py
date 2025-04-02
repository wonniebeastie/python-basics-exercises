# Using the following code, delete the `'mileage'` key and its associated value 
# from `car`.

# Solution 1
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

del car['mileage']
print(car) # {'type': 'sedan', 'color': 'blue', 'year': 2003}

"""
This solution uses the `del` keyword, which is used to delete objects. 
"""

# Solution 2
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

car.pop('mileage')
print(car) # {'type': 'sedan', 'color': 'blue', 'year': 2003}

"""
This solution uses the `.pop()` dictionary method, which removes a key-value
pair from a dictionary and returns the value. 
"""
