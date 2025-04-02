# Rewrite `car` as a list of lists in which each nested list contains two 
# elements that represent the corresponding key/value pairs.
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

# Rewrite
car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

# Using a list comprehension with unpacking technique 
nested_car_attributes_list = [[key, value] for key, value in car.items()]
print(nested_car_attributes_list) 
# [['type', 'sedan'], ['color', 'blue'], ['year', 2003]]
