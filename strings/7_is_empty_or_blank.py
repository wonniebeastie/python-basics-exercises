# Write an `is_empty_or_blank` function to determine whether a string is either
# empty or consists entirely of spaces.

# LS Solution
def is_empty_or_blank(s):
    """
    - Most concise
    - Potential gotcha: Only handles space characters, not other whitespace 
      types
    """
    return not s.strip(' ')

# My solutions
def is_empty_or_blank2(s):
    """
    Pros: 
    - Most Pythonic (recommended by LSBot) approach leveraging truthiness
    - More explicit handling of both empty & whitespace cases
    - Handles all types of whitespace characters (spaces, tabs, newlines)
    """
    return not s or s.isspace()

def is_empty_or_blank3(s):
    """
    - Most explicit & readable for beginners
    - Clear intentioin with direct empty string comparison
    - Handles all whitespace characters like the previous function
    """
    return s == '' or s.isspace()


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

print(is_empty_or_blank2('mars'))  # False
print(is_empty_or_blank2('  '))    # True
print(is_empty_or_blank2(''))      # True

print(is_empty_or_blank3('mars'))  # False
print(is_empty_or_blank3('  '))    # True
print(is_empty_or_blank3(''))      # True
