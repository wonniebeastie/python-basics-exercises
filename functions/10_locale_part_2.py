# Similar to the previous exercise, write a function that extracts the region 
# code from a locale. For example:
def extract_region(locale):
    return locale[3:5]

def extract_region2(locale):
    return locale.split('.')[0].split('_')[1]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

print(extract_region2('en_US.UTF-8'))    # US
print(extract_region2('en_GB.UTF-8'))    # GB
print(extract_region2('ko_KR.UTF-16'))   # KR
