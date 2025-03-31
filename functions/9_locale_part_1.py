# Write a function that extracts the language code from a locale. A locale is a
# combination of a language code, a region, and usually also a character set, 
# e.g en_US.UTF-8.
def extract_language(locale):
    """
    This solution returns the extracted slice of the characters from index 0 to
    1 (stopping values for slicing syntax are exclusive). 
    """
    return locale[0:2]

def extract_language2(locale):
    """
    This solution splits the argument string into a list using `'_'` as the 
    delimiter so that it will split into the first two characters then the
    rest of the string after the `'_'` into a list. Then it returns the value
    of the first element of that list.
    """
    return locale.split('_')[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

print(extract_language2('en_US.UTF-8'))      # en
print(extract_language2('en_GB.UTF-8'))      # en
print(extract_language2('ko_KR.UTF-16'))     # ko
