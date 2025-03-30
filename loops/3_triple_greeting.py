# Write a loop that prints the value of the greeting variable three times.
greeting = 'Aloha!'

for _ in range(3):
    print(greeting)

# Aloha!
# Aloha!
# Aloha!

"""
A `for` loop can be used with a range object to print the value referred to by
the `greeting` variable a specific number of times. The range object generates
3 elements, which is why it prints 3 times in this code.
"""

count = 0
while count < 3:
    print(greeting)
    count += 1

# Aloha!
# Aloha!
# Aloha!
"""
A `while` loop can be used to print the value assigned to `greeting` 3 times. A
counter variable (`count`) is initialized on line 17 and incremented by 1 on
line 20 until the condition for the `while` loop is no longer truthy. 
"""
