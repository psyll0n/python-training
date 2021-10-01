#!/usr/bin/env python3
# Datetime module basics.

from datetime import date, time, datetime

# TODO: Create a new date object.
d1 = date.today()
print(d1)


# TODO: Create a new time object.
t1 = time(12, 30, 00)
print(t1)


# TODO: Create a new datetime object.
dt1 = datetime.now()
print(dt1)


# TODO: Access various components of the datetime objects.
print(d1.day)
print(d1.month)
print(d1.year)

print(t1.hour)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(dt1.month)
print(dt1.weekday())
print(days[dt1.weekday()])


# TODO: To modify the values of the date and time objects, use the replace() method.
d1 = d1.replace(year=2020, month=1, day=31)
t1 = t1.replace(hour=5)
dt1 = dt1.replace(year=2021, month=9, day=27, hour=2)
