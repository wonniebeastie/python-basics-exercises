# Write a function that compares the length of two strings. It should return -1
# if the first string is shorter, 1 if the second string is shorter, and 0 if 
# they're of equal length. For example:
"""
I: a string
I: another string
O: -1, 0, or 1

✱ QUESTIONS ✱
- 

✱ RULES ✱
- -1 must be returned if the first string is shorter
- 1 must be returned if the second string is shorter
- 0 must be returned if the argument strings are of equal length

✱ EXAMPLES / TEST CASES ✱
- 'patience', 'perseverance' -> -1
- 'strength', 'dignity' -> 1
- 'humor', 'grace -> 0

✱ DS ✱
- 

✱ ALGORITHM ✱
I: `str1`, `str2`
[] if the length of str1 is shorter than the length of str2:
    [] return -1
[] else if the length of str1 is longer than the length of str2:
    [] return 1
[] else:
    [x] return 0
"""
def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0 

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0
