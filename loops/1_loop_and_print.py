# Add some code inside the following for loop to print the current value of num
# on each iteration. Before you execute the code: What sequence of numbers do 
# you expect to be printed?

for num in range(0, 11, 2):
    print(num)

"""
I predict that the numbers that will be printed will be:
0, 2, 4, 6, 8, 10

For range objects with 3 arguments, the first is the starting value (inclusive),
the second is the stopping value (exclusive), and the last is the step value,
which indicates the number of steps to take between each number.
"""
