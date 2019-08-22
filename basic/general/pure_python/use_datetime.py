# # `datetime` module examples
#
# This module will allow you to get the current date/time and calculate deltas, among many functions.
#
# If you want to use the current timestamp as a table name suffix in SQL, you'll need to do a bit of string manipulation, as shown in the creation of the `clean_timestamp` variable.

from datetime import datetime

# Get the timestamp for right now
this_instant = datetime.now()

# Let's inspect this item's type and representation
print(type(this_instant))
this_instant

# Turn this timestamp into a string and the format as you want
timestamp_str = str(this_instant)
print(timestamp_str)

# +
# Extract date and time
the_date, the_time = timestamp_str.split(" ")
print(the_day)
print(the_time)

# Omit the miliseconds in the time
the_time = the_time.split(".")[0]
print(the_time)

# +
# Replace unwanted characters in the_time with an underscore
the_time = the_time.replace(":", "_")
    
# Do the same for the date's dash
the_date = the_date.replace("-", "_")
    
clean_timestamp = f"{the_date}_{the_time}"
# -

print(clean_timestamp)
