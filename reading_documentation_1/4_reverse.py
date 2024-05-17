# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

og_string = 'hello'


print(reversed(og_string))  # <reversed object at 0x104409990>

"""
I tried to use the built-in function `reversed()` with it not realizing 
that the returned value is lazy.

I had to go back and read up on what lazy sequences are & learned that lazy
sequences are not computed/loaded into memory until they're specifically 
requested - meaning I have to some other way, like a list constructor
(for collections) or a string method like `string.join()` to make the returned
value be usable.
"""

reversed_string = og_string[::-1]
print(reversed_string)  # olleh

"""
I also tried to see if I can use the `list.reverse()` method but realized that
they can only be used with lists, not strings. 

The slicing method looked strange to me, as a beginner, and I could not have
come up with it on my own. 
"""


