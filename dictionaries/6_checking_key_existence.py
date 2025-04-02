# Check whether the keys 'name' and 'grade' exist in the following dictionary:
student = {
    'id': 123,
    'grade': 'B',
}

# Solution 1
print('name' in student)  # False
print('grade' in student) # True

"""
Solution 1 uses the `in` membership operator to check if the keys exist in the
`student` dictionary. When applied to dictionaries, this operator checks for
the specified value among the keys of the specified dictionary only.
"""

# Solution 2
print(student.get('name', 'False')) # False
print(True if student.get('grade') else False) # True 
"""
This solution uses the `.get()` dictionary method. 

For the `'name'` key, this
method is used to try to fetch the value associated with the key - and return
`False` if the key does not exist.False

For the `'grade'` key, a ternary expression is used to return `True` if the key
exists in the `student` dictionary, and `False` if it does not.
"""
