# Write a function that checks whether a string starts with a specific prefix.
"""
I: a string (full string)
I: a string (prefix)
O: True or False

✱ QUESTIONS ✱
- can the prefix string be of any length?

✱ RULES ✱
- check whether the first string argument starts with the second string
  argument.

✱ EXAMPLES / TEST CASES ✱
- "launch", "la" -> True
- "school", "sah" -> False
- "school", "sch" -> True

✱ DS ✱
- potential use of string slicing & length to determine stopping point (to 
  address potential edge cases of shorter or longer prefix strings)

✱ ALGORITHM ✱
I: `txt`, `prefix`
[] initialize `stop_value` - with length of prefix
[] use slicing to determine if a sliced portion of the txt string (use stop_
   value as stopping point) is the same value as the prefix string.
[] return as True or False
"""
def starts_with(txt, prefix):
    stop_value = len(prefix)
    return txt[:stop_value] == prefix

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# LS Solution
def starts_with(string, prefix):
    return string.startswith(prefix)
