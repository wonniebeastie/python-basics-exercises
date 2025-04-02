"""
We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe 
game. However, we encountered an issue, as whenever we change a value in one 
nested list, all nested lists are affected. Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
"""
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list[:])

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

print(id(matrix[0]))
print(id(matrix[0][0]))
print(id(matrix[0][1]))
print(id(matrix[0][2]))

"""
The bug was because when the `sub_list` was being appended to `matrix`, the
reference to the same list object was being added 3 times. So modifying one 
also impacted the others.

Slicing can be used to create a copy of `sub_list`, which creates a new object
that is identical in value, and append that to the `matrix` list.

Other methods of creating copies like the `.copy()` list method can be used to
achieve the same thing.
"""
