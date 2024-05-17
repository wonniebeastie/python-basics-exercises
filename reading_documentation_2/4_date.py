# Using the datetime module in Python, how would you obtain the current date
# and time?

import datetime

current_datetime = datetime.datetime.now()

print(current_datetime)  # 2024-04-17 13:51:37.082679

"""
- The `datetime.datetime.now` method returns current local date & time, which 
is very useful for many things, like logging or timestamping events.

- [Documentation](https://docs.python.org/3/library/datetime.html) for datetime module.

- To make it more readable/easier:

`from datetime import datetime
current_datetime = datetime.now()

print(current_datetime)`
"""