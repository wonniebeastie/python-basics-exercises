# Modify the following code so the loop continues iterating until the user 
# inputs 'yes'.
while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print('We will not take anything other than a "yes".')
