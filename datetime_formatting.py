#!/usr/bin/env python3

import datetime


# Create a datetime for today.
now = datetime.datetime.now()


# TODO: Print various day and month formatting.
# print(now.strftime("%a, %A %w, %d"))
# print(now.strftime("%b, %B %m"))


# TODO: Print various time formatting.
# print(now.strftime("%H, %I, %M %S, %p"))

# TODO: Locale-specific formatting.
# print(now.strftime("%c"))
# print(now.strftime("%X"))


# TODO: Short date format (m/d/y).
output = now.strftime("%m/%d/%y")


# TODO: Long date format (Day, number, Month, Year).
output = now.strftime("%A %d, %B %Y")
print("today is: ", output)


# TODO: Short date and time format (m/d/y, h:mm:ss AM/PM).
output = now.strftime("%m/%d/%y %I:%M %p")
print("today is: ", output)
