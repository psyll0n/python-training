#!/usr/bin/env python3

import datetime


# Create some date objects.
dt1 = datetime.datetime(2019, 6, 10)
dt2 = datetime.datetime(2021, 9, 27)


# Dates and times can be compared.
print(dt1 < dt2)
print(dt1 > dt2)


# Subtracting one date from another creates a timedelta object.
delta = dt2 - dt1
print(delta)

# Timedeltas have attributes that are useful for dealing with date and time differences.
print(delta.days)
print(delta.seconds)

# Timedeltas can be used to perform date math.
now = datetime.datetime.now()
oneyear = datetime.timedelta(days=365)
oneweek = datetime.timedelta(weeks=1)


print("One year from now will be: ", now + oneyear)
print("One week from now will be: ", now + oneweek)
print("One week ago was: ", now - oneweek)
