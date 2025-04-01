# Count the number of elements in scores that are 100 or above.
scores = [96, 47, 113, 89, 100, 102]

# Solution 1
high_scores = []

for score in scores:
    if score >= 100:
        high_scores.append(scores)

print(len(high_scores)) # 3

"""
This solution creates an empty list `high_scores` to append only the scores
that are 100 or above as a `for` loop iterates through the elements of the
`scores` list.
"""

# Solution 2
high_scores = [score for score in scores if score >= 100]
print(len(high_scores)) # 3

"""
This solution utilizes a list comprehension to apply filtering to include only
scores 100 and above in the new list that is returned.

Then the length of that list is printed.
"""

# LS Solution
count = 0

for score in scores:
    if score >= 100:
        count += 1

print(count)  # 3

"""
This solution initializes a `count` variable that is assigned 0 to increment
as a `for` loop iterates through the elements in `scores`. Whenever a score is
100 or above, the integer assigned to `count` is incremented by 1.
"""
