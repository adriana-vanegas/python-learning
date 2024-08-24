# Time Stamps
# Used mostly to calculated duration

import time

# Number of seconds since January 1st 1970
print(time.time())



from datetime import datetime

dt = datetime(2024,1,1)
now = datetime.now()
print(dt)
print(now)

# To parse/convert a datetime string
# If we're dealing with a string
convert = datetime.strptime("2018/01/01","%Y/%m/%d")
# %Y uppercase Y means four numbers for year
# %m lowercase m means 2 numbers for month
# find the directives here: https://docs.python.org/3/library/datetime.html
print(convert)

# We can convert a timestamp to a datetime

conversion = datetime.fromtimestamp(time.time())
print(conversion)


print(f"{dt.year}/{dt.month}")

# To format date times:
# Convert a datetime object into a string
print(dt.strftime("%Y/%m"))

# To compare datetime objects
print(dt > now)

# Time delta
# Calculate the difference between different datetimes
from datetime import timedelta

duration = now - dt
print(duration)
print(f"Days: ",duration.days)
print(f"Seconds: ",duration.seconds) # This is equivalent to the hour+min+sec

print(f"Total Seconds: ",duration.total_seconds()) #Total seconds incl day, hour, min, sec


# Add time to datetime
datetime_example = datetime(2024,1,1)+timedelta(days = 1, seconds=1000)
print(datetime_example)
