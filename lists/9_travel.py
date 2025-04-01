"""
The `destinations` list contains a list of travel destinations.

Write a function that, without using the built-in `in` operator, checks whether 
a specific destination is included within `destinations`. For example: When 
checking whether `'Barcelona'` is contained in `destinations`, the expected output 
is `True`, whereas the expected output for `'Nashville'` is `False`.

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False
"""
"""
I: a string (of a single destination)
I: a list (of destinations)
O: True or False

✱ QUESTIONS ✱
- 

✱ RULES ✱
- the `in` operator cannot be used
- function must check whether a specific destination is included in the input
  list/2nd argument

✱ EXAMPLES / TEST CASES ✱
- 'Barcelona', destinations -> True
- 'Nashville', destinations -> False

✱ DS ✱
- 

✱ ALGORITHM ✱
I: `place`, `travel_destinations`
[] for destination in travel_destinations:
    [] if destination is same in value as place:
        [] return True
    [] else return False 
"""
def contains(place, travel_destinations):
    for city in travel_destinations:
        if city == place:
            return True

    return False

def contains2(place, travel_destinations):
    if travel_destinations.count(place):
        return True
    else:
        return False

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

print(contains2('Barcelona', destinations))  # True
print(contains2('Nashville', destinations))  # False
