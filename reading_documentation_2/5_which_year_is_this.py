# The Python documentation for the datetime module provides two attributes to 
# retrieve the year from a date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?

"""
The `year` attribute indicates just the year while `isocalendar` method returns 
year, week, and weekday in a tuple.

In most scenarios, use the `year` attribute.
"""