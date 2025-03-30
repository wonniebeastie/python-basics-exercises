# The following code keeps looping forever. (You can hit Ctrl-C to stop it.) 
# Why does the loop keep running? Modify it so that it stops after the first 
# iteration.
while True:
    print("and on")
    break

"""
The code keeps looping because there is no stopping condition for the `while`
loop. `while` loops goes on looping as long as its conditional expression
remains truthy. In this code, the conditional expression is `True` which means
that it will always remain truthy so the body of the loop will run forever.

I modified the code to add a `break` statement, which causes the loop to 
terminate. 
"""
