"""
Use a `for` loop to iterate over the `numbers` dictionary and return a list 
containing each number divided by 2 as an integer. The result should be 
truncated to an integer. Assign the returned list to a variable named 
`half_numbers` and print its value using `print`.
"""
numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
# Expected output: [50, 25, 12]

"""
I: a dictionary
O: a list

✱ QUESTIONS ✱
- 

✱ RULES ✱
- `for` loop must be used
- output list must only have the values from the input dictionary, but
  divided by 2, truncated to an integer (no decimals)
- output list must be assigned to variable named `half_numbers`
- list must be printed

✱ DS ✱
- an empty list to contain the new values

✱ ALGORITHM ✱
I: `num_dict`
[] initialize empty list - `half_numbers`
[] for each number in a list of of the values from the num_dict dictionary:
    [] divide the number in half
    [] convert it to an integer
    [] add it to half_numbers
[] print half_numbers
"""
# Solution 1
def divide_by_two(num_dict):
    half_numbers = []

    for num in num_dict.values():
        half_numbers.append(int(num / 2)) 

    print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

divide_by_two(numbers) # [50, 25, 12]


# Solution 2
def divide_by_two_2(num_dict):
    half_numbers = [int(num/2) for num in num_dict.values()]
    print(half_numbers)

divide_by_two_2(numbers) # [50, 25, 12]


# LS Solution
half_numbers = []
for value in numbers.values():
    half_numbers.append(value // 2)

print(half_numbers)

"""
The floor/integer division operator `//` can be used to return an integer 
instead of a float in place of the `int()` constructor.
"""
