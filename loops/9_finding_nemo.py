# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'.
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

"""
This solution works because the entire body of the loop executes with each
iteration. So it will first print the element assigned to the loop variable
then check if the current element in that iteration is equal to `'Nemo'`
before going onto the next iteration. 

So when it gets to `'Nemo'`, it will print that and terminate the loop before
`'Bruce'` can be printed.
"""

# FURTHER EXPLORATION
index = 0

while index < len(fish_list):
    print(fish_list[index])
    if fish_list[index] == 'Nemo':
        break
    index += 1
