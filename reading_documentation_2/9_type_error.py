# The following code raises a TypeError:
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, then use the 
# resulting error message to determine exactly what is wrong. (You don't have 
# to fix this code.)
"""
When run, this code outputs:
    length_of_tweet = len(tweet + 5)
                          ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

A TypeError indicates that an operation or function was applied to an object of
inappropriate type. In this case, the `+` operator was used to attempt to 
concatenate the `5` to the value referred to by the variable `tweet`. This did
not work since `5` in an integer type while the value of `tweet` is a string 
type.
"""
