#!/usr/bin/env python3
"""datetime_usage.py - Demonstrates Python's datetime module basics.

The datetime module provides classes for manipulating dates and times:
- date: Represents a date (year, month, day)
- time: Represents a time (hour, minute, second, microsecond)
- datetime: Combines date and time
- timedelta: Represents a duration

Common operations:
- Creating date/time objects
- Accessing individual components
- Modifying values with replace()
- Getting current date/time
- Working with weekdays
"""

from datetime import date, time, datetime

# ===== Working with Dates =====

# Create a date object representing today
d1 = date.today()
print("Today's date:", d1)  # Format: YYYY-MM-DD

# ===== Working with Times =====

# Create a time object (hours, minutes, seconds)
t1 = time(12, 30, 00)
print("Time object:", t1)  # Format: HH:MM:SS

# ===== Working with Datetime (date + time combined) =====

# Create a datetime object with current date and time
dt1 = datetime.now()
print("Current datetime:", dt1)  # Format: YYYY-MM-DD HH:MM:SS.microseconds

# ===== Accessing Date Components =====

print("\nAccessing date components:")
print("Day:", d1.day)      # Day of month (1-31)
print("Month:", d1.month)  # Month (1-12)
print("Year:", d1.year)    # Year (e.g., 2025)

# ===== Accessing Time Components =====

print("\nAccessing time components:")
print("Hour:", t1.hour)  # Hour (0-23)

# ===== Working with Weekdays =====

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("\nWeekday information:")
print("Month:", dt1.month)
print("Weekday (0=Monday):", dt1.weekday())  # 0-6, where 0=Monday
print("Day name:", days[dt1.weekday()])      # Convert to day name

# ===== Modifying Date/Time Objects =====

# Note: date/time objects are immutable, so replace() returns a new object
print("\nModifying date/time objects with replace():")

# Modify date - returns a new date object
d1 = d1.replace(year=2020, month=1, day=31)
print("Modified date:", d1)

# Modify time - returns a new time object
t1 = t1.replace(hour=5)
print("Modified time:", t1)

# Modify datetime - can replace multiple components
dt1 = dt1.replace(year=2021, month=9, day=27, hour=2)
print("Modified datetime:", dt1)
