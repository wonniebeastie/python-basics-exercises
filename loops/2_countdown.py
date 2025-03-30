# The following code prints the numbers from 1 to 10. Modify it so that it 
# instead prints the numbers from 10 to 1 in descending order, followed by 
# 'Launch!'.
for i in range(10, 0, -1):
    print(i)

print('Launch!')

"""
The code was modified to use `10` as the starting value, `0` as the stopping
value (it is exclusive, so it will actually stop at `1` and not include the 0),
and `-1` as the step value to generate the numbers in reverse order. 
"""
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Launch!
